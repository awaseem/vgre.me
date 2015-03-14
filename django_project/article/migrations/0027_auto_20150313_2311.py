# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0026_auto_20150312_1954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='created_image',
        ),
        migrations.RemoveField(
            model_name='article',
            name='created_name',
        ),
        migrations.RemoveField(
            model_name='article',
            name='created_occupation',
        ),
    ]
