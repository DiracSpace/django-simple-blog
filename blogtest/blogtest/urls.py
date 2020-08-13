from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^about/$', views.about),
    re_path(r'^$', views.home),
]
