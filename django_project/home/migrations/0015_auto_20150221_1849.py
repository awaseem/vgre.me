# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20150221_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='footer_cover',
            field=models.URLField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='header',
            name='header_cover',
            field=models.URLField(),
            preserve_default=True,
        ),
    ]
