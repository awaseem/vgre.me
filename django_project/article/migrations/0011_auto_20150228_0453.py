# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_auto_20150228_0446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sections',
            name='section_body',
            field=tinymce.models.HTMLField(help_text=b'Enter a paragraph for this section', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sections',
            name='section_heading',
            field=models.CharField(help_text=b'This sections heading', max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
