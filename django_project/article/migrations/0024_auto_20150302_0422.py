# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0023_auto_20150228_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sections',
            name='gif_subheading',
            field=models.CharField(help_text=b'Enter the sub-heading for this sections gif', max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
