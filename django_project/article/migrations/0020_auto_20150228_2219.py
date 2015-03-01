# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0019_auto_20150228_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='game_review_back_cover',
            field=models.URLField(default=b'http://gearnuke.com/wp-content/uploads/2015/01/FC4_PREVIEWS_KARMA_EVENT_02.0.jpg', help_text=b'Enter an image for the back game cover (homepage)'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='game_review_cover',
            field=models.URLField(default=b'http://gearnuke.com/wp-content/uploads/2015/01/FC4_PREVIEWS_KARMA_EVENT_02.0.jpg', help_text=b'Enter an image for the game cover (homepage)'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='game_review_description',
            field=models.CharField(default=b'test', help_text=b'Enter a short description about the game review (homepage)', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='game_theme',
            field=models.CharField(default=b'Blue', help_text=b'Enter a color theme for this review', max_length=20, choices=[(b'#337ab7', b'Blue'), (b'#5cb85c', b'Green'), (b'#f0ad4e', b'Yellow'), (b'#5bc0de', b'Light Blue'), (b'#d9534f', b'Red')]),
            preserve_default=True,
        ),
    ]
