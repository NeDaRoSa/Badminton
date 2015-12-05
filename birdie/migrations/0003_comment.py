# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('birdie', '0002_auto_20151205_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('text', models.CharField(max_length=1024)),
                ('timestamp', models.DateTimeField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='comments')),
                ('game', models.ForeignKey(to='birdie.Game', related_name='comments')),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
    ]
