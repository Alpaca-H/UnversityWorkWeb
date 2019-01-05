# -*- coding:utf-8 -*-
__author__ = 'hzj'


#xadmin_setting
"""
1.添加要显示的类
list_display = ['']  
2.要查询的类
search_fields = ['',]
3.要筛选的列
list_filter = ['']
4.定义底部标题与头部标题
class GlobalSetting(object):
    site_title = '鲸之网'   #设置头标题
    site_footer = '鲸之网'  #设置脚标题
    menu_style = 'accordion' #设置菜单格式
xadmin.site.register(views.CommAdminView, GlobalSetting)
5.更改xadmin后台的主题
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView,BaseSetting)
"""
import xadmin
from .models import  EamilVerifyRecord,Banner
from news.models import Comments
from xadmin import views

# 配置主题
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView,BaseSetting)


# 配置标题
class GlobalSetting(object):
    site_title = 'Search | System'   #设置头标题
    site_footer = 'Alpaca Code'  #设置脚标题
    menu_style = 'accordion' #设置菜单格式
xadmin.site.register(views.CommAdminView, GlobalSetting)


# 验证码
class EamilVerifyRecordXadmin(object):

    list_display = ['code','email','send_type','send_time']
    list_filter =  ['send_type','send_time']

# 轮播图
class BannerXadmin(object):
    pass


# 多级评论
class CommentsXadmin(object):
    pass


xadmin.site.register(Banner, BannerXadmin)
xadmin.site.register(EamilVerifyRecord, EamilVerifyRecordXadmin)
xadmin.site.register(Comments, CommentsXadmin)