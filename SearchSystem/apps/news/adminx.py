# -*- coding:utf-8 -*-
__author__ = 'hzj'

import xadmin
from .models import  HupuNbaNews,XlNews,ZbbNews,TxVideo,Saicheng
from xadmin import views




#虎扑新闻
class HupuNbaNewsXadmin(object):
    pass


#直播吧新闻
class ZbbNewsXadmin(object):
    pass

# 腾讯视频
class TxVideoXadmin(object):
    pass

# 新浪新闻
class XlNewsXadmin(object):
    pass


class SaichengXadmin(object):
    pass

xadmin.site.register(HupuNbaNews,HupuNbaNewsXadmin)
xadmin.site.register(ZbbNews,ZbbNewsXadmin)
xadmin.site.register(TxVideo,TxVideoXadmin)
xadmin.site.register(XlNews,XlNewsXadmin)
xadmin.site.register(Saicheng,SaichengXadmin)