# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=49)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('ifsc', models.CharField(max_length=11, serialize=False, primary_key=True)),
                ('branch', models.CharField(max_length=74)),
                ('address', models.CharField(max_length=195)),
                ('city', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=26)),
                ('bank_id', models.ForeignKey(to='bank.Banks')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
