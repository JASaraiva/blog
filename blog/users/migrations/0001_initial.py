# Generated by Django 3.0.2 on 2020-02-01 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=50)),
                ('cellphone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=20)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]