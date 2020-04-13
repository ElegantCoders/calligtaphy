from django.shortcuts import render
from .models import Banner, Article, Categoty, FriendlyLink
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.db.models import Q
from django.views.generic.base import View

# Create your views here.

'''
后续改进成前后端分离代码
'''


# # 请求方式类
# class MethodGetOrPost(object):
#     def __init__(self, req_json_obj):
#         self.req_json_obj = req_json_obj
#
#     def get(self, request):
#         if request.method == 'GET':
#             print(type(self.req_json_obj))
#             return HttpResponse(self.req_json_obj)
#
#     def post(self):
#         if self.req_json_obj.method == 'POST':
#             return HttpResponse(self.req_json_obj)
#
#
# @csrf_exempt
# def index(request):
#
#     obj = Banner.objects.all()
#     for i in obj:
#         print(i)
#     banner_list = serializers.serialize('json', Banner.objects.all())
#     return MethodGetOrPost(banner_list).get(request)

# 首页显示
def index(request):
    # 获取轮播图对象
    banner_list = Banner.objects.all()
    # 获取文章分类对象  得到所有一级类目   返回前6个分类
    categoty1 = Categoty.objects.filter(category_type=1).order_by('-add_time')[:6]
    # 获取文章分类对象  得到所有二级类目   返回前10个分类
    categoty2 = Categoty.objects.filter(category_type=2).order_by('-add_time')
    # 获取文章对象
    article = Article.objects.all()
    # 获取友情链接对象   返回前10个分类
    friendly_link_list = FriendlyLink.objects.all().order_by('-add_time')[:10]
    # 最新发布    进行时间倒序排序且只返回10条数据
    article_publish_recently_list = article.order_by('-pub_date')[:10]
    # 热门文章    进行筛选出最大浏览量的数据返回10条
    popular_articles_list = article.order_by('-views')[:10]

    ctx = {
        "categoty1": categoty1,  # 分类一级类目
        "categoty2": categoty2,  # 文章分类二级类目
        "banner_list": banner_list,  # 轮播图
        "article_publish_recently_list": article_publish_recently_list,  # 最新发布
        "popular_articles_list": popular_articles_list,  # 热门文章
        "friendly_link_list": friendly_link_list,  # 友情链接
    }
    # print(type(ctx))
    return render(request, 'index.html', ctx)




# 搜索功能
@csrf_exempt
def search(request):
    kw = request.POST.get('keyword')
    err_msg = '抱歉！未搜索到您要查询的信息。'

    article_list = Article.objects.filter(Q(title__icontains=kw) | Q(cont_synopsis__icontains=kw))
    ctx = {
        "kw": kw,
        "search_article_list": article_list,
        "err_msg": err_msg,
    }
    return render(request, 'two_list.html', ctx)


# 文章详情
def article_detail(request, pid):
    article = Article.objects.get(id=pid)
    # 每点击一次浏览量+1
    article.views += 1
    article.save()
    '''
    获取当前访问的ip   对比数据库   无  ip地址存库   浏览量+1  IpArticle.is_visit=Ture
    获取当前访问的ip   对比数据库   有  查IpArticle.is_visit=0  浏览量+1  IpArticle.is_visit=Ture
    '''
    ctx = {
        "article_list": article,
    }
    return render(request, 'details.html', ctx)


# 二级类别  文章列表展示
def categoty_article_list(request, aid):
    article_list = Article.objects.filter(category=aid)  # 获取二级分类下所有文字

    if article_list:
        ctx = {
            "two_article_list": article_list,
            "categoty_article_list": categoty_article_list,
        }
        return render(request, 'two_list.html', ctx)
    # elif categoty_article_list:
    #     ctx = {
    #         "categoty_article_list": categoty_article_list,
    #     }
    #     return render(request, 'one_list.html', ctx)
    else:
        return render(request, 'err404.html')


# 一级分类  文章列表展示
def one_categoty_article_list(request, aid):
    one_categoty_article_list = Categoty.objects.filter(parent_category=aid).all()  # 获取一级分类下的所有二级分类关联的文章

    categoty_article_list = []  # 所有二级分类关联的文章列表
    for categoty_article in one_categoty_article_list:
        categoty_article = Article.objects.filter(category=categoty_article.id)
        categoty_article_list.append(categoty_article)
    if categoty_article_list:
        ctx = {
            "categoty_article_list": categoty_article_list,
        }
        return render(request, 'one_list.html', ctx)
    else:
        return render(request, 'err404.html')


def popular_articles_list(request):
    popular_articles_list = Article.objects.all().order_by('-views')

    ctx = {
        "popular_articles_list": popular_articles_list,
    }

    return render(request, 'popular_list.html', ctx)