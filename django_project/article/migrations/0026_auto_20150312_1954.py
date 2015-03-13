# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0025_auto_20150302_0425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='game_menu_color',
        ),
        migrations.RemoveField(
            model_name='article',
            name='game_theme',
        ),
    ]
