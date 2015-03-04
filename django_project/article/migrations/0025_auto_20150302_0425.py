# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0024_auto_20150302_0422'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='created_image',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='created_occupation',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
