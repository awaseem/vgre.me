# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20150216_0634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='header',
            name='button_text',
        ),
        migrations.AddField(
            model_name='header',
            name='theme_choice',
            field=models.CharField(default=b'btn-default', max_length=20, choices=[(b'btn-default', b'Blue'), (b'btn-success', b'Green'), (b'btn-info', b'Light Blue'), (b'btn-warning', b'Yellow'), (b'btn-danger', b'Red')]),
            preserve_default=True,
        ),
    ]
