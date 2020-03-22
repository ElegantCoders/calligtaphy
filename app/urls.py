from django.conf.urls import include, url
from app import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
]

# url('ueditor/', include('DjangoUeditor.urls')),