# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'

# 独立使用django的model
import sys
import os
# 先初始化环境
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+'../')  # 当前目录的上级目录
# 某些需求，比如连接数据库，依赖setting。
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SearchSystem.settings')  # 单独使用model必须拿过来 manage中

import django
django.setup()


def random_color():
    import random
    color_number = str(str(random.randint(0,6)))+str(str(random.randint(0,6)))+str(str(random.randint(0,6)))+str(str(random.randint(0,6)))+str(str(random.randint(0,6)))+str(str(random.randint(0,6)))
    return color_number


def charts_Bar_display():  #柱形图展示
    from pyecharts import Bar
    from opperation.models import TxNba1718CgCj
    ss = TxNba1718CgCj._meta.fields  #获取所有字段  遍历之后.name  得到字段名列表
    attr = []
    for i in ss:
        attr.append(i.name)
    v1 = list(TxNba1718CgCj.objects.values_list()[0])
    v2 = list(TxNba1718CgCj.objects.values_list()[1])
    bar = Bar("Bar chart", "precipitation and evaporation one year")
    bar.add("precipitation", attr, v1, mark_line=["average"], mark_point=["max", "min"])
    bar.add("evaporation", attr, v2, mark_line=["average"], mark_point=["max", "min"])
    bar.render("")


# from  opperation.models import TxNba1718CgCj
# ss = TxNba1718CgCj.objects.values("paiming")
# print(ss)

def charts_Pie_display():
    from pyecharts import Pie
    from opperation.models import TxNba1718CgCj
    ss = TxNba1718CgCj._meta.fields  # 获取所有字段  遍历之后.name  得到字段名列表
    attr = []
    for i in ss:
        attr.append(i.name)
    v1 = list(TxNba1718CgCj.objects.values_list()[0])
    v2 = list(TxNba1718CgCj.objects.values_list()[1])
    pie  = Pie("test_pie")
    pie.add("test_Pie",attr,v1,radius=[0,100],is_label_show=True)
    pie.add("test_Pie2", attr, v2, radius=[0, 100], is_label_show=True)
    pie.render("")


def charts_Radar_display():
    from pyecharts import Radar
    from opperation.models import TxNba1718CgCj
    ss = TxNba1718CgCj._meta.fields  #获取字段
    attr=[]
    for i in ss:
        if i.name == "defen_selected":
            q = (i.name,'50')
            attr.append(q)
        elif i.name == "zhugong":
            q = (i.name, '50')
            attr.append(q)
        elif i.name == "qiangduan":
            q = (i.name, '50')
            attr.append(q)
        elif i.name == "lanban":
            q = (i.name, '50')
            attr.append(q)
        elif i.name == "gaimao":
            q = (i.name, '50')
            attr.append(q)
    v3 = [list(TxNba1718CgCj.objects.values('defen_selected','zhugong','qiangduan','lanban','gaimao')[0].values())]
    v4 = [list(TxNba1718CgCj.objects.values('defen_selected', 'zhugong', 'qiangduan', 'lanban', 'gaimao')[1].values())]
    radar = Radar()
    radar.config(attr)
    radar.add("test_Pie",v3,is_splitline_show=True,is_axisline_show=True,label_color=[random_color()],is_area_show=True)
    radar.add("1", v4, is_splitline_show=True, is_axisline_show=True,label_color=[random_color()],legend_selectedmode='single')
    radar.render("")



if __name__ == '__main__':
    # charts_Bar_display()
    # charts_Pie_display()
    charts_Radar_display()
    random_color()