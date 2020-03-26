from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^article_detail/(?P<pid>\d+)/$', views.article_detail, name='article_detail')
]
