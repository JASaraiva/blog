# Generated by Django 3.0.2 on 2020-02-01 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
