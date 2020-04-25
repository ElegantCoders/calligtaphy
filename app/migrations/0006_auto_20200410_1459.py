# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200322_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_carousel',
            field=models.BooleanField(verbose_name='轮播图是否显示此文章', default=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_cover',
            field=models.ImageField(verbose_name='文章封面', default=None, upload_to='static/images/article_cover'),
        ),
        migrations.AlterField(
            model_name='article',
            name='cont_synopsis',
            field=models.TextField(verbose_name='内容摘要（简述）', max_length=300),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='文章主体内容', default=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_delete',
            field=models.BooleanField(verbose_name='是否删除此文章，勾选为删除，页面不显示此文章！', default=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(verbose_name='发布日期', default=datetime.datetime(2020, 4, 10, 14, 59, 48, 511623)),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(verbose_name='标题', max_length=30),
        ),
        migrations.AlterField(
            model_name='article',
            name='views',
            field=models.PositiveIntegerField(verbose_name='浏览量', default=0),
        ),
        migrations.AlterField(
            model_name='banner',
            name='add_time',
            field=models.DateTimeField(verbose_name='添加时间', default=datetime.datetime(2020, 4, 10, 14, 59, 48, 510625)),
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_cover',
            field=models.ImageField(verbose_name='轮播图', upload_to='static/images/banner_cover'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='is_active',
            field=models.BooleanField(verbose_name='是否生效', default=False, help_text='是否设置为首页默认显示的轮播图'),
        ),
        migrations.AlterField(
            model_name='categoty',
            name='add_time',
            field=models.DateTimeField(verbose_name='添加时间', default=datetime.datetime(2020, 4, 10, 14, 59, 48, 509628)),
        ),
        migrations.AlterField(
            model_name='categoty',
            name='category_type',
            field=models.IntegerField(verbose_name='类目级别', choices=[(1, '一级类目'), (2, '二级类目')], help_text='类目级别'),
        ),
        migrations.AlterField(
            model_name='friendlylink',
            name='add_time',
            field=models.DateTimeField(verbose_name='添加时间', default=datetime.datetime(2020, 4, 10, 14, 59, 48, 511623)),
        ),
    ]
