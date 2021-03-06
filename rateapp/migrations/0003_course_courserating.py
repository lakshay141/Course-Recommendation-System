# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-25 08:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rateapp', '0002_auto_20170324_2110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200)),
                ('course_id', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='CourseRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rateapp.Course')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rateapp.UserTable')),
            ],
        ),
    ]
