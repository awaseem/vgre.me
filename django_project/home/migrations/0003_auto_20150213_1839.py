# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20150213_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='button_text',
            field=models.CharField(default=b'test', max_length=5, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='header',
            name='sub_heading',
            field=models.CharField(default=b'test', max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='header',
            name='summary_text',
            field=models.CharField(default=b'test', max_length=400, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='header',
            name='title_text',
            field=models.CharField(default=b'test', max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
