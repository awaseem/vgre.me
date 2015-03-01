# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0017_auto_20150228_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='footer_image',
            field=models.URLField(default=b'http://i.imgur.com/iPYPXkE.jpg', help_text=b'Enter the URL for a footer image'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='header_image',
            field=models.URLField(default=b'http://i.imgur.com/iPYPXkE.jpg', help_text=b'Enter the URL for a header image'),
            preserve_default=True,
        ),
    ]
