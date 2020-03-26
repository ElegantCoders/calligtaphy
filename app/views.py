from django.shortcuts import render
from .models import Banner, Article, Categoty, FriendlyLink
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

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
    # 获取文章对象
    article = Article.objects.all()
    # 最新发布    进行时间倒序排序且只返回10条数据
    article_publish_recently_list = article.order_by('-pub_date')[:10]
    # 热门文章    进行筛选出最大浏览量的数据返回10条
    popular_articles_list = article.order_by('-views')[:2]

    ctx = {
        "banner_list": banner_list,
        "article_publish_recently_list": article_publish_recently_list,
        "popular_articles_list": popular_articles_list,
    }

    return render(request, 'index.html', ctx)


def article_detail(request, pid):
    article = Article.objects.get(id=pid)
    # 每点击一次浏览量+1
    article.views += 1
    article.save()

    ctx = {
        "article_list": article,
    }
    return render(request, 'details.html', ctx)
