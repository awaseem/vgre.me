# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_header_main_heading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='summary_text',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
