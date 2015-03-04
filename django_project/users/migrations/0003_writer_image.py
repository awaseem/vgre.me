# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150301_0616'),
    ]

    operations = [
        migrations.AddField(
            model_name='writer',
            name='image',
            field=models.URLField(default=b'http://www.fastcoexist.com/multisite_files/coexist/imagecache/1280/poster/2013/01/1681317-poster-1280-bill-gates.jpg'),
            preserve_default=True,
        ),
    ]
