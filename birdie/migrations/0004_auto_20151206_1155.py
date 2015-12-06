# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('birdie', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='url',
            field=models.URLField(max_length=128, default='www.test.com'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='game',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, to='birdie.Location'),
        ),
        migrations.AlterField(
            model_name='game',
            name='organiser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, related_name='organised_games', to=settings.AUTH_USER_MODEL),
        ),
    ]
