# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20150221_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='theme_name',
            field=models.CharField(help_text=b'Give this theme a name', max_length=50),
            preserve_default=True,
        ),
    ]
