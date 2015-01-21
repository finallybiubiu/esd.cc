# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_segmentfault_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='segmentfault_blog',
            name='name',
            field=models.CharField(max_length=36, blank=True),
            preserve_default=True,
        ),
    ]
