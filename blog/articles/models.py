from django.db import models
from photos.models import Photo
from comments.models import Comment
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200,null=False)
    content = models.TextField(null=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comment, blank=True)
    images = models.ManyToManyField(Photo,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.title)
