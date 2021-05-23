# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_delete_branches'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('ifsc', models.CharField(max_length=11, serialize=False, primary_key=True)),
                ('branch', models.CharField(max_length=74)),
                ('address', models.CharField(max_length=195)),
                ('city', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=26)),
                ('bank_id', models.ForeignKey(default=b'0000000', to='bank.Bank')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
