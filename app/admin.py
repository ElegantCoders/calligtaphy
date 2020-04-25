from django.contrib import admin

# Register your models here.
from app.models import *


class ArticleAdmin(admin.ModelAdmin):
    '''设置列表可显示的字段'''
    list_display = ('category', 'title', 'author', 'pub_date', 'views', 'is_carousel', 'is_delete',)

    '''设置过滤选项'''
    list_filter = ('author',)

    '''每页显示条目数'''
    list_per_page = 10

    # '''按日期月份筛选'''
    # date_hierarchy = 'pub_date'

    '''按发布日期排序'''
    ordering = ('-pub_date',)


class CategotyAdmin(admin.ModelAdmin):
    '''设置列表可显示的字段'''
    list_display = ('category_type', 'name', 'parent_category', 'add_time',)

    '''每页显示条目数'''
    list_per_page = 10

    '''设置过滤选项'''
    list_filter = ('category_type',)


class BannerAdmin(admin.ModelAdmin):
    '''设置列表可显示的字段'''
    list_display = ('title', 'add_time',)

    '''每页显示条目数'''
    list_per_page = 10


class FriendlyLinkAdmin(admin.ModelAdmin):
    '''设置列表可显示的字段'''
    list_display = ('title', 'link', 'add_time',)

    '''每页显示条目数'''
    list_per_page = 10


# 注册模型
admin.site.register(Article, ArticleAdmin)
admin.site.register(Categoty, CategotyAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(FriendlyLink, FriendlyLinkAdmin)

