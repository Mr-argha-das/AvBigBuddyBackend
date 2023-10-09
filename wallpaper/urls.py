"""
URL configuration for wallpaper project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from .views import (UserLsit, UserAdd, UserLogin, UserData)
from .tagsview import (TagsLsit, TagsAdd, TagsByBannerId)
from .bannerview import (BannerAdd, BannerList)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user-list', UserLsit.as_view(), name='user-list'),
    path('api/v1/user-singup', UserAdd.as_view(), name='user-singup'),
    path('api/v1/user-login', UserLogin.as_view(), name="user-login"),
    path('api/v1/tags-list', TagsLsit.as_view(), name="tags-list"),
    path('api/v1/tags-add', TagsAdd.as_view(), name="tags-add"),
    path('api/v1/user-data', UserData.as_view(), name="user-data"),
    path('api/v1/banners-data', BannerList.as_view(), name="banners-data"), 
    path('api/v1/tags-by-id',TagsByBannerId.as_view(), name="tags-by-id"),

]
