# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20150213_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='button_text',
            field=models.CharField(max_length=5, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='header',
            name='sub_heading',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='header',
            name='summary_text',
            field=models.CharField(max_length=400, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='header',
            name='title_text',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
