# Generated by Django 3.0.2 on 2020-02-01 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
        ('articles', '0002_auto_20200201_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='comments',
            field=models.ManyToManyField(blank=True, to='comments.Comment'),
        ),
    ]
