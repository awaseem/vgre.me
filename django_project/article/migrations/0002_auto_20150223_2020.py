# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sections',
            name='image_subheading',
            field=models.CharField(help_text=b'Enter the sub-heading for the URL', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sections',
            name='image_url',
            field=models.URLField(help_text=b'Enter the URL for the article image', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sections',
            name='section_body',
            field=tinymce.models.HTMLField(help_text=b'Enter a paragraph for this section'),
            preserve_default=True,
        ),
    ]
