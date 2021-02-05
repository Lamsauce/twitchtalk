from django.db import models

# Create your models here.
class Thread(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=3000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)