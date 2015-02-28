# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_auto_20150228_0453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_url', models.URLField(help_text=b'Enter the URL for this sections media ', blank=True)),
                ('image_subheading', models.CharField(help_text=b'Enter the sub-heading for this sections media', max_length=100, blank=True)),
                ('section', models.ForeignKey(to='article.Sections')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='sections',
            name='media_subheading',
        ),
        migrations.RemoveField(
            model_name='sections',
            name='media_type',
        ),
        migrations.RemoveField(
            model_name='sections',
            name='media_url',
        ),
    ]
