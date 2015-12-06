# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birdie', '0004_auto_20151206_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='embed_url',
            field=models.URLField(null=True, max_length=1024),
        ),
    ]
