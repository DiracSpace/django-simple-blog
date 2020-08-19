from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from . import views

"""
Detects url input from users and calls function
from views
"""

urlpatterns = [
    path('admin/', admin.site.urls, name="adminpanel"),
    re_path(r'^about/$', views.about, name="about"),
    re_path(r'^$', views.home, name="home"),
    re_path(r'^accounts/', include('accounts.urls')),
    re_path(r'^articles/', include('articles.urls')),
]

# for appending the static filepath
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
