# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200410_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='is_delete',
            field=models.BooleanField(verbose_name='是否删除此文章，勾选为删除，页面不显示此文章！', default=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(verbose_name='发布日期', default=datetime.datetime(2020, 4, 10, 15, 15, 38, 46686)),
        ),
        migrations.AlterField(
            model_name='banner',
            name='add_time',
            field=models.DateTimeField(verbose_name='添加时间', default=datetime.datetime(2020, 4, 10, 15, 15, 38, 45700)),
        ),
        migrations.AlterField(
            model_name='categoty',
            name='add_time',
            field=models.DateTimeField(verbose_name='添加时间', default=datetime.datetime(2020, 4, 10, 15, 15, 38, 45700)),
        ),
        migrations.AlterField(
            model_name='friendlylink',
            name='add_time',
            field=models.DateTimeField(verbose_name='添加时间', default=datetime.datetime(2020, 4, 10, 15, 15, 38, 47694)),
        ),
    ]
