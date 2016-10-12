"""URLS for forum app"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<post_id>\d+)/$', views.post_view, name='post'),
    url(r'^post/(?P<post_id>\d+)/edit$', views.edit_post, name='edit_post'),
    url(r'^new_post/$', views.new_post, name='new_post'),
    url(r'^user/(?P<user_name>[\w\-@.+_]+)/$', views.user_view, name='user'),
    url(r'^userlist/$', views.userlist, name='userlist'),
]
