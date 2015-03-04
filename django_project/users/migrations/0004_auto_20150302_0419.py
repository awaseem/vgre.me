# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_writer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writer',
            name='image',
            field=models.URLField(),
            preserve_default=True,
        ),
    ]
