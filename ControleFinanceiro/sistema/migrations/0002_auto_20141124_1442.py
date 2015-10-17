# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemsistema',
            name='participantes',
        ),
        migrations.RemoveField(
            model_name='itemsistema',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='ItemSistema',
        ),
        migrations.AlterField(
            model_name='ganho',
            name='tipo',
            field=models.CharField(max_length=100),
        ),
    ]
