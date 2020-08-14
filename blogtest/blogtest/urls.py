from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

"""
Detects url input from users and calls function
from views
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^about/$', views.about),
    re_path(r'^$', views.home),
    re_path(r'^articles/', include('articles.urls')),
]

# for appending the static filepath
urlpatterns += staticfiles_urlpatterns()
