# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20150227_0326'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 28, 2, 26, 24, 80350, tzinfo=utc), verbose_name=b'Date published'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='published_status',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='review_status',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
