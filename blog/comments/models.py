from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    title = models.CharField(max_length=100,default='artigo')
    comment = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
