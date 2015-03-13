# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_auto_20150312_1944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='theme',
            old_name='current_header',
            new_name='current_theme',
        ),
    ]
