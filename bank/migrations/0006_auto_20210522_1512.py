# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0005_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='bank_id',
            field=models.ForeignKey(to='bank.Bank'),
        ),
    ]
