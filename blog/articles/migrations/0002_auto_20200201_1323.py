# Generated by Django 3.0.2 on 2020-02-01 16:23

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos', '0001_initial'),
        ('comments', '0001_initial'),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.contrib.auth.models.User, to=settings.AUTH_USER_MODEL)),
                ('comments', models.ManyToManyField(to='comments.Comment')),
                ('images', models.ManyToManyField(to='photos.Photo')),
            ],
        ),
        migrations.DeleteModel(
            name='Artigo',
        ),
    ]