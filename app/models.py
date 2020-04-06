from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


# 分类
class Categoty(models.Model):
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目")
    )

    name = models.CharField("分类名称", max_length=20, default='')
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")
    parent_category = models.ForeignKey('self', null=True, blank=True, verbose_name="关联父类目", help_text="父目录",
                                        related_name="sub_cat", default='')
    is_tab = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否在首页导航栏显示")
    add_time = models.DateTimeField(default=datetime.now(), verbose_name=u"添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '书法分类'
        verbose_name_plural = verbose_name


# 轮播图
class Banner(models.Model):
    title = models.CharField('标题', max_length=30)
    banner_cover = models.ImageField('轮播图', upload_to='static/images/banner_cover')
    link_url = models.URLField('图片链接', max_length=300)
    idx = models.IntegerField('索引')
    is_active = models.BooleanField('是否生效', default=False, help_text="是否设置为首页默认显示的轮播图")
    add_time = models.DateTimeField(default=datetime.now(), verbose_name=u"添加时间")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name


# 文章
class Article(models.Model):
    category = models.ForeignKey(Categoty, verbose_name="书法分类", default=None)
    title = models.CharField('标题', max_length=50)
    author = models.CharField('作者', max_length=10)
    cont_synopsis = models.CharField('内容摘要', max_length=300)
    content = RichTextUploadingField(default='', verbose_name='主体内容')
    pub_date = models.DateTimeField('发布日期', default=datetime.now())
    article_cover = models.ImageField('博客封面', upload_to='static/images/article_cover', default=None)
    views = models.PositiveIntegerField('浏览量', default=0)
    is_delete = models.BooleanField('是否显示此文章', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name


# 友情链接
class FriendlyLink(models.Model):
    title = models.CharField('标题', max_length=50)
    link = models.URLField('链接', max_length=50, default='')
    add_time = models.DateTimeField(default=datetime.now(), verbose_name=u"添加时间")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name



