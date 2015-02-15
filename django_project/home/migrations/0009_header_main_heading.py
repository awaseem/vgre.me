# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20150213_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='header',
            name='main_heading',
            field=models.CharField(default='nothing', max_length=10),
            preserve_default=False,
        ),
    ]
