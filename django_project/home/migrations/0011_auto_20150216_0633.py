# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20150215_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='summary_text',
            field=tinymce.models.HTMLField(),
            preserve_default=True,
        ),
    ]
