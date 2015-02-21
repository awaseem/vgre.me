# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20150221_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='header',
            name='footer_cover',
            field=models.URLField(default=b'test.url'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='header',
            name='header_cover',
            field=models.URLField(default=b'test.url'),
            preserve_default=True,
        ),
    ]
