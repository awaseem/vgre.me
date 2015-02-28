# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0012_auto_20150228_0457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='section',
        ),
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.AddField(
            model_name='sections',
            name='gif_subheading',
            field=models.URLField(help_text=b'Enter the sub-heading for this sections gif', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sections',
            name='gif_url',
            field=models.URLField(help_text=b'Enter the URL for this sections gif (html video only)', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sections',
            name='image_subheading',
            field=models.CharField(help_text=b'Enter the sub-heading for this sections image', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sections',
            name='image_url',
            field=models.URLField(help_text=b'Enter the URL for this sections image ', blank=True),
            preserve_default=True,
        ),
    ]
