# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_segmentfault_blog_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='V2EX',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tid', models.IntegerField(max_length=10)),
                ('node', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=50)),
                ('click', models.IntegerField(max_length=10)),
                ('mark', models.IntegerField(max_length=10)),
                ('thank', models.IntegerField(max_length=10)),
                ('comment', models.IntegerField(max_length=10, blank=True)),
                ('idate', models.DateField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
