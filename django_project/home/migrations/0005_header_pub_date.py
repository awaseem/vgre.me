# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20150213_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='header',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 13, 19, 28, 56, 444853, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
    ]
