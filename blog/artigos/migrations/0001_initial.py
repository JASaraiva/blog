# Generated by Django 3.0.2 on 2020-02-01 14:55

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
        ('photos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('Status', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.contrib.auth.models.User, to=settings.AUTH_USER_MODEL)),
                ('comments', models.ManyToManyField(to='comments.Comment')),
                ('images', models.ManyToManyField(to='photos.Photo')),
            ],
        ),
    ]
