from django.conf.urls import url
from django.contrib import admin
from .views import (
    posts_list,
    posts_update,
    posts_delete,
    posts_detail,
    posts_create,
)
urlpatterns = [
    url(r'^$', posts_list,name='list'),
    url(r'^create/$', posts_create,name='create'),
    url(r'^(?P<slug>[\w-]+)/$', posts_detail, name='detail'),
    # url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/delete/$', posts_delete, name='delete'),
    url(r'^(?P<slug>[\w-]+)/edit/$', posts_update, name='update'),

]
