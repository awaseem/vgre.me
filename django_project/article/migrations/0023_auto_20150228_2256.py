# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0022_article_game_menu_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='game_review_back_cover',
            field=models.URLField(help_text=b'Enter an image for the back game cover (homepage)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='game_review_cover',
            field=models.URLField(help_text=b'Enter an image for the game cover (homepage)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='game_review_description',
            field=models.CharField(help_text=b'Enter a short description about the game review (homepage)', max_length=100),
            preserve_default=True,
        ),
    ]
