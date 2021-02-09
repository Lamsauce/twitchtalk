from django.db import models #imports models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User #imports user

# Create your models here.
class Thread(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=3000)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['-created_at']

class Comment(models.Model):
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)

class Game(models.Model):
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 10000)
    twitch_url = models.URLField(max_length = 200)

    def __str__(self):
        return f"{self.title}"