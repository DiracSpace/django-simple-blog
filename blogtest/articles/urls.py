from django.urls import path, re_path
from . import views

"""
urls for the articles app
"""
app_name = 'articles'

urlpatterns = [
    re_path(r'^$', views.articles_list, name='list'),
    re_path(r'^create/$', views.create_article, name='create'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.articles_detail, name='detail'),
]
