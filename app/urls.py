from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),  # 首页
    url(r'^article_detail/(?P<pid>\d+)/$', views.article_detail, name='article_detail'),  # 文章详情
    url(r'^search/$', views.search, name='search'),  # 搜索
    url(r'^categoty_article_list/(?P<aid>\d+)/$', views.categoty_article_list, name='categoty_article_list'),  # 分类列表
]
