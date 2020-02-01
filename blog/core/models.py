from django.db import models

class Core(models.Model):
    title = ''


    def __str__(self):
        return self.title

