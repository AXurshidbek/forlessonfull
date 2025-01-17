from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updatet_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

