# coding:utf-8
from django.conf import settings
# from django.conf.urls.defaults import patterns, include, url
from django.conf.urls import patterns, include, url
from blog.feeds import LatestPostFeed

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

handler404 = 'views.handler404'

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^$', 'views.home'),
                       # url(r'^aliyun_verify_3c2a8c9eb497880e48d0569136c03476.html/$', 'views.aliyun'),
                       url(r'^archives/$', 'views.archives'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.MEDIA_ROOT, }),  # TODO 用nginx配置代替
                       url('^contact/$', 'views.contact'),
                       url('^about/$', 'views.about'),

                       # blog
                       url(r'^post/(?P<pid>\d+)/', 'blog.views.show_post'),
                       url(r'^tag/(?P<name>.+)/$', 'blog.views.list_by_tag'),
                       url(r'^feed/$', LatestPostFeed()),
                       url(r'^upload-image/', 'blog.views.upload_image'),

)



