# -*- coding:utf-8 -*-
__author__ = 'hzj'

from django import template
register = template.Library()

@register.filter()
def cut_column(value,dd):  #分栏功能,根据传来的List以及截取的条件，分栏
    return value[dd:12]