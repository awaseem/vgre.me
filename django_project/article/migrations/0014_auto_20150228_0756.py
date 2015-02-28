# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0013_auto_20150228_0511'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='created_name',
            field=models.CharField(default=b'test', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='created_user',
            field=models.CharField(default=b'test', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='last_modified_user',
            field=models.CharField(default=b'test', max_length=200),
            preserve_default=True,
        ),
    ]
