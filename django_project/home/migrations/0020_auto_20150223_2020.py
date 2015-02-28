# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20150221_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='summary_text',
            field=tinymce.models.HTMLField(help_text=b'Please enter a summary for the reviews section'),
            preserve_default=True,
        ),
    ]
