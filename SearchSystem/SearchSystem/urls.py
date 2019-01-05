"""SearchSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from extra_apps import xadmin
from django.views.generic import TemplateView
from user.views import LoginView,RegisterView,NopasswordView,ResgisterActiveView,changePasswordView,CommentsView,UserParseView,UserUploadSettingView
from opperation.views import DataDisplay,NoBackView,chartDisplayView,TestView,someMatchView,saichengView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('xadmin/', xadmin.site.urls),# 跳转后台

    path('',TemplateView.as_view(template_name="first.html"),name="index"), # 跳转首页

    path('zhuce/',RegisterView.as_view(),name="register"), # 跳转注册页面
    path('nopassword/', NopasswordView.as_view(), name="nopassword"),  # 跳转到忘记密码页面
    path('captcha/',include('captcha.urls')), # 验证码
    path('active/<str:code>/',ResgisterActiveView.as_view(),name="activeResgister"), # 激活链接
    path('change/<str:code>/',changePasswordView.as_view(),name="changePassword"),  # 修改密码

    # operation
    path('data/', DataDisplay.as_view(), name="DataDisplay"),  # 跳转数据页面

    # news
    path('', include('news.urls')),  # 跳转新闻urls.py

    path('chart/',chartDisplayView.as_view(),name='chartDisplay'),  # 图表

    path("404Response/",NoBackView.as_view(),name="NoBack"), # 没有返回

    path("zhanshi/",LoginView.as_view(),name="zhanshi"),  # 展示

    path("setting_info/",TestView.as_view(),name="Test"),

    path("match/",someMatchView.as_view(),name="match"),


    path("about/",TemplateView.as_view(template_name="zhnashi.html"),name="zhanshi_nologin"),

    path('comment/',CommentsView.as_view(),name="comments"),

    path('parse/',UserParseView.as_view(),name="parses"),

    path('UploadHead/',UserUploadSettingView.as_view(),name="upload"),

    path('saicheng/',saichengView.as_view(),name="saicheng")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
