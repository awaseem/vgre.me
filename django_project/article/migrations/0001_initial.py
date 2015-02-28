# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Date created')),
                ('game_name', models.CharField(help_text=b'Name of the game you are reviewing', max_length=100)),
                ('article_heading', models.CharField(help_text=b'Article heading', max_length=50)),
                ('article_sub_heading', models.CharField(help_text=b'Article sub heading', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sections',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('section_heading', models.CharField(help_text=b'This sections heading', max_length=50)),
                ('section_body', models.TextField(help_text=b'This sections body')),
                ('article', models.ForeignKey(to='article.Article')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
