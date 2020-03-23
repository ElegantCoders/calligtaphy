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
    article_list = Article.objects.all().order_by('-pub_date')[:2]

    ctx = {
        "banner_list": banner_list,
        "article_list": article_list,
    }

    return render(request, 'index.html', ctx)
