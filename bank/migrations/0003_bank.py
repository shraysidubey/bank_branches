# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_auto_20210522_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('b_id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=49)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
