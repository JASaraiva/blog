# Generated by Django 3.0.2 on 2020-02-01 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20200201_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
