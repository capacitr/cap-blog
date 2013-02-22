from django.conf.urls.defaults import patterns, include, url

import views

urlpatterns = patterns('',
    url(r'^(?P<post_slug>[\w-]+)/$', views.get_post, name='blog_post'),
)

