# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20150312_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'date published')),
                ('theme_name', models.CharField(help_text=b'Give this theme a name', max_length=50)),
                ('theme_choice', models.CharField(default=b'btn-primary', help_text=b'Color theme for the featured game', max_length=20, verbose_name=b'Theme', choices=[(b'btn-primary', b'Blue'), (b'btn-success', b'Green'), (b'btn-info', b'Light Blue'), (b'btn-warning', b'Yellow'), (b'btn-danger', b'Red')])),
                ('menu_background', models.CharField(default=b'#337ab7', max_length=10)),
                ('home_header_cover', models.URLField(help_text=b"Please enter A URL of a picture you'd like for the home page header")),
                ('home_footer_cover', models.URLField(help_text=b"Please enter a URL of a picture you'd like for the home page footer")),
                ('search_header_cover', models.URLField(help_text=b"Please enter a URL of a picture you'd like for the search page header")),
                ('search_footer_cover', models.URLField(help_text=b"Please enter a URL of a picture you'd like for the search page footer")),
                ('current_header', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Header',
        ),
    ]
