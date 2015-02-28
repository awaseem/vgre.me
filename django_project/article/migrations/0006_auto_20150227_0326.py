# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20150227_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sections',
            name='section_heading',
            field=models.CharField(help_text=b'This sections heading', max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
