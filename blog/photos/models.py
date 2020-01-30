from django.db import models

class Photo(models.Model):
    img = models.CharField(max_length=150)
    