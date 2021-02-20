from django.db import models #imports models
from datetime import date
from django.contrib.auth.models import User #imports user

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 10000)
    twitch_url = models.URLField(max_length = 200)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.title}"

class Thread(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=3000)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['-created_at']

class Comment(models.Model):
    body = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"USER: {self.user} COMMENTED: '{self.body}'"

    class Meta:
        ordering = ['-created_at']