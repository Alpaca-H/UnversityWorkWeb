# -*- coding:utf-8 -*-
__author__ = 'hzj'
from .views import  NewsDisplay,NewsAllView,NewsListView,Top100View
from  django.urls import path

app_name = 'news'


urlpatterns = [
    path('news_display/<str:type>/', NewsDisplay.as_view(), name ="newsDisplay"),# 跳转新闻页面
    path('news_detail/<int:id>/', NewsAllView.as_view(), name = "newsAll"),#新闻详情页面
    path("newsList/", NewsListView.as_view(), name="newsList"), #跳转新闻列表页
    path('Top100/', Top100View.as_view(), name='top100'),  # 跳转视频Top100
]