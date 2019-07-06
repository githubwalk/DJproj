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

    
    path('RecruitApp/<str:currentCity>/', RecruitApp_v.index), #主页

    # 魏 07/06
    path('RecruitApp/search/<str:currentCity>/',RecruitApp_v.gotoClickedProfession),
    # end

    # 07/06 11:30 add by 黄涣升
    # 关于
    path('RecruitApp/inside/aboutusabout/', RecruitApp_v.aboutusAbout), # 关于-智联招聘
    path('RecruitApp/inside/jobsZhaoPin/', RecruitApp_v.jobsZhaoPin),# 关于-人才招聘
    path('RecruitApp/inside/aboutuscontact/', RecruitApp_v.aboutusContact),# 关于-联系方式
    path('RecruitApp/inside/aboutuscontact/', RecruitApp_v.aboutusContact),# 关于-联系方式

    # 帮助
    path('RecruitApp/inside/joinus/', RecruitApp_v.joinUs),# 帮助-加入我们
    path('RecruitApp/inside/customerService/', RecruitApp_v.customerService),# 帮助-客户服务
    path('RecruitApp/inside/law/', RecruitApp_v.law),# 帮助-法律声明
    path('RecruitApp/inside/secrecy/', RecruitApp_v.secrecy),# 帮助-隐私政策
    path('RecruitApp/inside/invoiceSystem/', RecruitApp_v.invoiceSystem),# 帮助-发票制度
    
    # end


    # 唐&川 07/06
    path('login', RecruitApp_v.login),
    path('register', RecruitApp_v.register),
    # end

    # 璇 07/06
    path('RecruitApp/per/resume/', RecruitApp_v.perResume),
    path('RecruitApp/per/schedule/', RecruitApp_v.perSchedule),
    path('RecruitApp/per/resumemodels/', RecruitApp_v.resumeModels),
    path('RecruitApp/per/question/<int:num>/', RecruitApp_v.workHotspots),
    # end


    # 骅 07/06
    path('apply/applyCheckedJobs/', RecruitApp_v.applyCheckedJobs),
    # end
]
