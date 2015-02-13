# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_header_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='header',
            name='current_header',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
