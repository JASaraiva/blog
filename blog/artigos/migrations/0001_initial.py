# Generated by Django 3.0.2 on 2020-01-30 00:41

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
        ('users', '0001_initial'),
        ('photos', '0001_initial'),
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
                ('author', models.ForeignKey(on_delete=users.models.User, to='users.User')),
                ('comments', models.ManyToManyField(to='comments.Comment')),
                ('images', models.ManyToManyField(to='photos.Photo')),
            ],
        ),
    ]
