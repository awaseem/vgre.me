# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20150221_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='header',
            name='menu_background',
            field=models.CharField(default=b'#337ab7', max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='header',
            name='footer_cover',
            field=models.URLField(help_text=b"Please enter a URL of a picture you'd like for the footer"),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='header',
            name='header_cover',
            field=models.URLField(help_text=b"Please enter A URL of a picture you'd like for the header"),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='header',
            name='main_heading',
            field=models.CharField(help_text=b'Please enter a main header', max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='header',
            name='sub_heading',
            field=models.CharField(help_text=b'Please enter a sub heading', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='header',
            name='summary_text',
            field=models.TextField(help_text=b'Please enter a summary for the reviews section'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='header',
            name='theme_choice',
            field=models.CharField(default=b'btn-default', max_length=20, verbose_name=b'Theme', choices=[(b'btn-primary', b'Blue'), (b'btn-success', b'Green'), (b'btn-info', b'Light Blue'), (b'btn-warning', b'Yellow'), (b'btn-danger', b'Red')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='header',
            name='title_text',
            field=models.CharField(help_text=b'Please enter a heading for the reviews section', max_length=200),
            preserve_default=True,
        ),
    ]
