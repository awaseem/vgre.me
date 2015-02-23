# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20150221_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='theme_choice',
            field=models.CharField(default=b'btn-primary', help_text=b'Color theme for the featured game', max_length=20, verbose_name=b'Theme', choices=[(b'btn-primary', b'Blue'), (b'btn-success', b'Green'), (b'btn-info', b'Light Blue'), (b'btn-warning', b'Yellow'), (b'btn-danger', b'Red')]),
            preserve_default=True,
        ),
    ]
