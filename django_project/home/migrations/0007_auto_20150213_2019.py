# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_header_current_header'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
