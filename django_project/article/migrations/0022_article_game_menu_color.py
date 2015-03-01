# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0021_auto_20150228_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='game_menu_color',
            field=models.CharField(default=b'#337ab7', max_length=10),
            preserve_default=True,
        ),
    ]
