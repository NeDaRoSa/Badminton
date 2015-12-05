# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birdie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='address',
        ),
        migrations.AddField(
            model_name='location',
            name='description',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='postcode',
            field=models.CharField(default='GAA 001', max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='street',
            field=models.CharField(default='Bothwell street', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='street_number',
            field=models.IntegerField(default=123),
            preserve_default=False,
        ),
    ]
