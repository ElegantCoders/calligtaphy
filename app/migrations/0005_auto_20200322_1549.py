# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200322_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_cover',
            field=models.ImageField(verbose_name='博客封面', default=None, upload_to='media/static/images/article_cover'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(verbose_name='发布日期', default=datetime.datetime(2020, 3, 22, 15, 49, 33, 47446)),
        ),
        migrations.AlterField(
            model_name='banner',
            name='add_time',
            field=models.DateTimeField(verbose_name='添加时间', default=datetime.datetime(2020, 3, 22, 15, 49, 33, 47446)),
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_cover',
            field=models.ImageField(verbose_name='轮播图', upload_to='media/static/images/banner_cover'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='is_active',
            field=models.BooleanField(verbose_name='是否生效', default=False, help_text='是否在页面中显示轮播图'),
        ),
        migrations.AlterField(
            model_name='categoty',
            name='add_time',
            field=models.DateTimeField(verbose_name='添加时间', default=datetime.datetime(2020, 3, 22, 15, 49, 33, 46481)),
        ),
        migrations.AlterField(
            model_name='friendlylink',
            name='add_time',
            field=models.DateTimeField(verbose_name='添加时间', default=datetime.datetime(2020, 3, 22, 15, 49, 33, 48474)),
        ),
    ]
