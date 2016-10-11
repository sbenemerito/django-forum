from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150)
    date_added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title


class Comment(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    author = models.ForeignKey(User)
    post = models.ForeignKey(Post)

    def __str__(self):
        return self.text