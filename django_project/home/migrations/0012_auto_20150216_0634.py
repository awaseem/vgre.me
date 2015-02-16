# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20150216_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='summary_text',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
