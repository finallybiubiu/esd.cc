# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Segmentfault',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qid', models.BigIntegerField(max_length=16)),
                ('title', models.CharField(max_length=1000)),
                ('author', models.CharField(max_length=300)),
                ('mark', models.IntegerField(max_length=10)),
                ('view', models.IntegerField(max_length=10)),
                ('follow', models.IntegerField(max_length=10)),
                ('date', models.DateField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
