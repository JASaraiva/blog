from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=150)
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    cellphone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    role = models.CharField(max_length=10)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

