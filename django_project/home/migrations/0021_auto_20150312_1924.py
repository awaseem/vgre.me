# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20150223_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='header',
            name='footer_cover',
        ),
        migrations.RemoveField(
            model_name='header',
            name='header_cover',
        ),
        migrations.RemoveField(
            model_name='header',
            name='main_heading',
        ),
        migrations.RemoveField(
            model_name='header',
            name='sub_heading',
        ),
        migrations.RemoveField(
            model_name='header',
            name='summary_text',
        ),
        migrations.RemoveField(
            model_name='header',
            name='title_text',
        ),
        migrations.AddField(
            model_name='header',
            name='home_footer_cover',
            field=models.URLField(default=b'http://www.breastcancerwellness.org/bcw/wp-content/uploads/2014/09/test.gif', help_text=b"Please enter a URL of a picture you'd like for the home page footer"),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='header',
            name='home_header_cover',
            field=models.URLField(default=b'http://www.breastcancerwellness.org/bcw/wp-content/uploads/2014/09/test.gif', help_text=b"Please enter A URL of a picture you'd like for the home page header"),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='header',
            name='search_footer_cover',
            field=models.URLField(default=b'http://www.breastcancerwellness.org/bcw/wp-content/uploads/2014/09/test.gif', help_text=b"Please enter a URL of a picture you'd like for the search page footer"),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='header',
            name='search_header_cover',
            field=models.URLField(default=b'http://www.breastcancerwellness.org/bcw/wp-content/uploads/2014/09/test.gif', help_text=b"Please enter a URL of a picture you'd like for the search page header"),
            preserve_default=True,
        ),
    ]
