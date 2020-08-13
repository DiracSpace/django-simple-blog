from django.urls import path, re_path
from . import views

"""
redirects users with urls for the articles and displays them
"""
urlpatterns = [
    re_path(r'^$', views.articles_list),
]
