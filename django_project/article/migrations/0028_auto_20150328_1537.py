# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0027_auto_20150313_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='review_score',
            field=models.IntegerField(default=10, help_text=b'Enter a review score for this game', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]),
            preserve_default=True,
        ),
    ]
