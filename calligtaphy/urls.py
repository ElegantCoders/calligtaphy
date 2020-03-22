from django.conf.urls import include, url, static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'calligtaphy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('app.urls', namespace='blog', app_name='blog')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

# 没有这一句无法显示
urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)