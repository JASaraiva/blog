from django.db import models
from photos.models import Photo
from comments.models import Comment
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=User)
    comments = models.ManyToManyField(Comment)
    images = models.ManyToManyField(Photo)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
