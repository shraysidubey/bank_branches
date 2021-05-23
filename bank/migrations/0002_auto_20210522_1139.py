# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branches',
            name='bank_id',
        ),
        migrations.DeleteModel(
            name='Banks',
        ),
    ]
