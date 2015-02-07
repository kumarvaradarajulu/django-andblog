from django.conf.urls import patterns, include, url
from django.contrib import admin

import blog

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_andblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^blog/', include("blog.urls", namespace='blog')),
    (r'^ckeditor/', include('ckeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
