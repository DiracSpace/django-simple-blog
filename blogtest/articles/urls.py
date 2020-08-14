from django.urls import path, re_path
from . import views

"""
redirects users with urls for the articles and displays them
"""
app_name = 'articles'

urlpatterns = [
    re_path(r'^$', views.articles_list, name='list'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.articles_detail, name='detail'),
]
