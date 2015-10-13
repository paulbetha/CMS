# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Course_Name', models.CharField(max_length=200)),
                ('Credits', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Grade_Points', models.IntegerField(default=0)),
                ('Course_Name', models.ForeignKey(to='coursemanagement.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Student_Name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='enrollement',
            name='Student_Name',
            field=models.ForeignKey(to='coursemanagement.Student'),
        ),
    ]
