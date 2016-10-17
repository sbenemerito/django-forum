"""URLS for users app"""
from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    url(r'^login_view/$', login, {'template_name': 'users/login.html'}, name='login'),
    url(r'^login/$', views.login_view, name='login_view'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.logout_view, name='logout'),
]
