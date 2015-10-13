# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coursemanagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollement',
            name='Course_Name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='enrollement',
            name='Student_Name',
            field=models.CharField(max_length=200),
        ),
    ]
