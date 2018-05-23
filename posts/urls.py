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
    url(r'^list/$', posts_list),
    url(r'^create/$', posts_create),
    url(r'^(?P<id>\d+)/$', posts_detail),
    url(r'^delete/$', posts_delete),
    url(r'^(?P<id>\d+)/edit/$', posts_update, name='update'),

]
