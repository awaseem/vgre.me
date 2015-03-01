# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0016_auto_20150228_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='review_summary',
            field=models.TextField(help_text=b'Enter a summary for this game review'),
            preserve_default=True,
        ),
    ]
