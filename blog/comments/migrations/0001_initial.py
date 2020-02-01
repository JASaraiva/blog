# Generated by Django 3.0.2 on 2020-01-30 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ManyToManyField(to='users.User')),
            ],
        ),
    ]