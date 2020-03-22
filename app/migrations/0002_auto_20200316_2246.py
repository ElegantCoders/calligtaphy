# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(verbose_name='发布日期', default=datetime.datetime(2020, 3, 16, 22, 46, 15, 70001)),
        ),
        migrations.AlterField(
            model_name='categoty',
            name='parent_category',
            field=models.ForeignKey(verbose_name='关联父类目', blank=True, null=True, default='', help_text='父目录', related_name='sub_cat', to='app.Categoty'),
        ),
    ]
