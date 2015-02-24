from django.conf.urls import patterns, include, url
from django.contrib import admin
from poll.views import *
from django.views.defaults import *
from django.conf.urls.static import static
from django.conf import settings
import os
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^sayhi/$',sayhi),
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': settings.DEBUG}),
    (r'^bootstrap/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
    (r'^servermgmt/$',servermgmt),
    (r'^runcmd/$',runcmd),
    (r'^getcmdresult/$',getcmdresult),
    (r'^get_ip_list/$',get_ip_list),
    (r'^login/$',account_login),
    (r'^logout/$',logout),
    (r'^$',index),
    (r'^time/(\d+)/$',hour_ahead),
    (r'^dynamic/?(\d?)/$',dynamic_temp),
    (r'^dict/$',name_list),
)
# handler404 = "poll.views.handler404"

