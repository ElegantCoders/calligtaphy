# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200316_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='add_time',
            field=models.DateTimeField(verbose_name='添加时间', default=datetime.datetime(2020, 3, 16, 23, 0, 30, 318148)),
        ),
        migrations.AddField(
            model_name='categoty',
            name='add_time',
            field=models.DateTimeField(verbose_name='添加时间', default=datetime.datetime(2020, 3, 16, 23, 0, 30, 318148)),
        ),
        migrations.AddField(
            model_name='friendlylink',
            name='add_time',
            field=models.DateTimeField(verbose_name='添加时间', default=datetime.datetime(2020, 3, 16, 23, 0, 30, 319145)),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(verbose_name='发布日期', default=datetime.datetime(2020, 3, 16, 23, 0, 30, 319145)),
        ),
    ]
