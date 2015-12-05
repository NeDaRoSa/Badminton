# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=1024)),
                ('datetime', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('max_players', models.IntegerField()),
            ],
            options={
                'ordering': ['datetime'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=256)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='game',
            name='location',
            field=models.ForeignKey(to='birdie.Location'),
        ),
        migrations.AddField(
            model_name='game',
            name='organiser',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='organised_games'),
        ),
        migrations.AddField(
            model_name='game',
            name='players',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='games'),
        ),
    ]
