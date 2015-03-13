# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20150312_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='home_footer_cover',
            field=models.URLField(help_text=b"Please enter a URL of a picture you'd like for the home page footer"),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='header',
            name='home_header_cover',
            field=models.URLField(help_text=b"Please enter A URL of a picture you'd like for the home page header"),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='header',
            name='search_footer_cover',
            field=models.URLField(help_text=b"Please enter a URL of a picture you'd like for the search page footer"),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='header',
            name='search_header_cover',
            field=models.URLField(help_text=b"Please enter a URL of a picture you'd like for the search page header"),
            preserve_default=True,
        ),
    ]
