from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    comment = models.CharField(max_length=200)
    author = models.ManyToManyField(User)
    created = models.DateTimeField(auto_now_add=True)


