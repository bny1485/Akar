"""Akar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home, about_me, login_def, register_def, CV, Album
from Post.views import Post_detail, Post_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about-me/', about_me),
    path('cv/', CV),
    path('login/', login_def),
    path('register/', register_def),
    path('Album', Album),
    path('post-list', Post_list.as_view()),
    path('post-detail/<pk>', Post_detail.as_view())
]
