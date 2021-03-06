# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20150227_0321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='review_score',
            field=models.IntegerField(help_text=b'Enter a review score for this game', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='review_summary',
            field=tinymce.models.HTMLField(help_text=b'Enter a summary for this game review'),
            preserve_default=True,
        ),
    ]
