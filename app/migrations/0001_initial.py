# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='标题', max_length=50)),
                ('author', models.CharField(verbose_name='作者', max_length=10)),
                ('cont_synopsis', models.CharField(verbose_name='内容摘要', max_length=300)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='主体内容', default='')),
                ('pub_date', models.DateTimeField(verbose_name='发布日期', default=datetime.datetime(2020, 3, 16, 21, 54, 13, 500611))),
                ('article_cover', models.ImageField(verbose_name='博客封面', default=None, upload_to='static/images/article_cover')),
                ('views', models.IntegerField(verbose_name='浏览量', default=0)),
                ('is_delete', models.BooleanField(verbose_name='是否显示此文章', default=False)),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='标题', max_length=30)),
                ('banner_cover', models.ImageField(verbose_name='轮播图', upload_to='static/images/banner_cover')),
                ('link_url', models.URLField(verbose_name='图片链接', max_length=300)),
                ('idx', models.IntegerField(verbose_name='索引')),
                ('is_active', models.BooleanField(verbose_name='是否生效', default=False, help_text='是否在页面中显示文章')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
        migrations.CreateModel(
            name='Categoty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='分类名称', max_length=20, default='')),
                ('category_type', models.IntegerField(verbose_name='类目级别', choices=[(1, '一级类目'), (2, '二级类目'), (3, '三级类目')], help_text='类目级别')),
                ('is_tab', models.BooleanField(verbose_name='是否导航', default=False, help_text='是否在首页导航栏显示')),
                ('parent_category', models.ForeignKey(verbose_name='关联父类目级别', blank=True, null=True, default=None, help_text='父目录', related_name='sub_cat', to='app.Categoty')),
            ],
            options={
                'verbose_name': '书法分类',
                'verbose_name_plural': '书法分类',
            },
        ),
        migrations.CreateModel(
            name='FriendlyLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='标题', max_length=50)),
                ('link', models.URLField(verbose_name='链接', max_length=50, default='')),
            ],
            options={
                'verbose_name': '友情链接',
                'verbose_name_plural': '友情链接',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(verbose_name='书法分类', default=None, to='app.Categoty'),
        ),
    ]
