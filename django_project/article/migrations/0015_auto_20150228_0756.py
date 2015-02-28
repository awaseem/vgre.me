# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0014_auto_20150228_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_name',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='created_user',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='last_modified_user',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
