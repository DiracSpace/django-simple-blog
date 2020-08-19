from django.urls import path, re_path
from . import views

app_name = 'accounts'

urlpatterns = [
    re_path(r'^signup/$', views.usersignup, name="signup"),
    re_path(r'^login/$', views.userlogin, name="login"),
    re_path(r'^logout/$', views.userlogin, name='logout'),
]
