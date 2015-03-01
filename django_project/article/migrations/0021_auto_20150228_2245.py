# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0020_auto_20150228_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='game_theme',
            field=models.CharField(default=b'btn-primary', help_text=b'Enter a color theme for this review', max_length=20, choices=[(b'btn-primary', b'Blue'), (b'btn-success', b'Green'), (b'btn-info', b'Light Blue'), (b'btn-warning', b'Yellow'), (b'btn-danger', b'Red')]),
            preserve_default=True,
        ),
    ]
