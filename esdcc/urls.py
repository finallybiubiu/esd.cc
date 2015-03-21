from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'esdcc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.index'),
    url(r'^segmentfault/$', 'main.views.segmentfault_index'),
    url(r'^segmentfault_blog/$', 'main.views.segmentfault_blog_index'),
    url(r'^v2ex/$', 'main.views.v2ex_index'),
    url(r'^v2ex/click/$', 'main.views.v2ex_click'),
    url(r'^v2ex/mark/$', 'main.views.v2ex_mark'),
    url(r'^v2ex/thank/$', 'main.views.v2ex_thank'),
    url(r'^v2ex/comment/$', 'main.views.v2ex_comment'),
)
