# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20150223_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('review_summary', tinymce.models.HTMLField(help_text=b'Enter a summary for this game review')),
                ('review_score', models.IntegerField(help_text=b'Enter a review score for this game', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('article', models.ForeignKey(to='article.Article')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='sections',
            name='image_subheading',
        ),
        migrations.RemoveField(
            model_name='sections',
            name='image_url',
        ),
        migrations.AddField(
            model_name='sections',
            name='media_subheading',
            field=models.CharField(help_text=b'Enter the sub-heading for this sections media', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sections',
            name='media_type',
            field=models.CharField(blank=True, help_text=b'Enter the type of media for this section', max_length=5, choices=[(b'gif', b'Gif'), (b'image', b'Image')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sections',
            name='media_url',
            field=models.URLField(help_text=b'Enter the URL for this sections media ', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sections',
            name='section_body',
            field=tinymce.models.HTMLField(help_text=b'Enter a paragraph for this section', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sections',
            name='section_heading',
            field=models.CharField(help_text=b'This sections heading', max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
