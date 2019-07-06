"""DJproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

# 07/06 11:30 add by 黄涣升
from RecruitApp import views as RecruitApp_v
# end
urlpatterns = [
    path('admin/', admin.site.urls),

    # 07/06 11:30 add by 黄涣升
    path('RecruitApp/<str:currentCity>/', RecruitApp_v.index), #主页
    # end
]
