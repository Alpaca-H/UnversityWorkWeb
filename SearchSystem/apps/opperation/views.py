from django.shortcuts import render,HttpResponse
from django.views import View
from .models import TxNba1718CgCj,TxNba1718CgQb,TxNba1718JhCj,TxNba1718JhQb,TxNba1718JqCj,TxNba1718JqQb,TxNba1516CgCj,\
    TxNba1516CgQb,TxNba1516JhCj,TxNba1516JhQb,TxNba1516JqCj,TxNba1516JqQb,TxNba1617CgCj,TxNba1617CgQb,TxNba1617JhCj,\
    TxNba1617JhQb,TxNba1617JqCj,TxNba1617JqQb,PlayerInfo
from news.models import Saicheng
from pure_pagination.paginator import Paginator,EmptyPage,PageNotAnInteger
import datetime
REMOTE_HOST = "https://pyecharts.github.io/assets/js"
from pyecharts import Pie

from django.template import loader
import random

# Create your views here.

# 数据展示


class DataDisplay(View):
    def get(self, request):
        tx1718CgCj = TxNba1718CgCj.objects.all().values()
        try:
            page = request.GET.get('page',1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(tx1718CgCj,50,request=request)
        tx1718CgCj = p.page(page)

        # 加载1718全部
        tx1718CgQb = TxNba1718CgQb.objects.all().values()
        try:
            page2 = request.GET.get('page2', 1)
        except PageNotAnInteger:
            page2 = 1
        p2 = Paginator(tx1718CgQb, 50, request=request)
        tx1718CgQb = p2.page(page2)
        return render(request, 'data.html', {"tx1718CgCj":tx1718CgCj,"tx1718CgQb":tx1718CgQb})

    def post(self,request):
        nianfen = request.POST.get("nianfen","")
        saiji = request.POST.get("saiji","")
        if nianfen == "1516":
            if saiji == "季前赛":
                tx1516JqCj = TxNba1516JqCj.objects.all().values()
                page = 1
                p = Paginator(tx1516JqCj, 50, request=request)
                tx1516JqCj = p.page(page)

                tx1516jqQb = TxNba1516JqQb.objects.all().values()
                try:
                    page = request.GET.get('page', 1)
                except PageNotAnInteger:
                    page = 1
                p = Paginator(tx1516jqQb, 50, request=request)
                tx1516jqQb = p.page(page)
                return render(request, 'data.html', {'tx1516JqCj': tx1516JqCj, 'tx1516jqQb': tx1516jqQb})
            elif saiji == "季后赛":
                tx1516JhCj = TxNba1516JhCj.objects.all().values()
                page = 1
                p = Paginator(tx1516JhCj, 50, request=request)
                tx1516JhCj = p.page(page)

                tx1516jhQb = TxNba1516JhQb.objects.all().values()
                try:
                    page = request.GET.get('page', 1)
                except PageNotAnInteger:
                    page = 1
                p = Paginator(tx1516jhQb, 50, request=request)
                tx1516jhQb = p.page(page)
                return render(request, 'data.html', {'tx1516JhCj': tx1516JhCj, 'tx1516jhQb': tx1516jhQb})
            elif saiji == "常规赛":
                tx1516CgCj = TxNba1516CgCj.objects.all().values()
                page = 1
                p = Paginator(tx1516CgCj, 50, request=request)
                tx1516CgCj = p.page(page)

                tx1516CgQb = TxNba1516CgQb.objects.all().values()
                try:
                    page = request.GET.get('page', 1)
                except PageNotAnInteger:
                    page = 1
                p = Paginator(tx1516CgQb, 50, request=request)
                tx1516CgQb = p.page(page)
                return render(request, 'data.html', {'tx1516CgCj': tx1516CgCj, 'tx1516CgQb': tx1516CgQb})
        elif nianfen == "1617":
            if saiji == "季前赛":
                tx1617JqCj = TxNba1617JqCj.objects.all().values()
                page = 1
                p = Paginator(tx1617JqCj, 50, request=request)
                tx1617JqCj = p.page(page)

                tx1617jqQb = TxNba1617JqQb.objects.all().values()
                try:
                    page = request.GET.get('page', 1)
                except PageNotAnInteger:
                    page = 1
                p = Paginator(tx1617jqQb, 50, request=request)
                tx1617jqQb = p.page(page)
                return render(request, 'data.html', {'tx1617JqCj': tx1617JqCj, 'tx1617jqQb': tx1617jqQb})
            elif saiji == "季后赛":
                tx1617JhCj = TxNba1617JhCj.objects.all().values()
                page = 1
                p = Paginator(tx1617JhCj, 50, request=request)
                tx1617JhCj = p.page(page)

                tx1617JhQb = TxNba1617JhQb.objects.all().values()
                try:
                    page = request.GET.get('page', 1)
                except PageNotAnInteger:
                    page = 1
                p = Paginator(tx1617JhQb, 50, request=request)
                tx1617JhQb = p.page(page)
                return render(request, 'data.html', {'tx1617JhCj': tx1617JhCj, 'tx1617JhQb': tx1617JhQb})
            elif saiji == "常规赛":
                tx1617CgCj = TxNba1617CgCj.objects.all().values()
                page = 1
                p = Paginator(tx1617CgCj, 50, request=request)
                tx1617CgCj = p.page(page)

                tx1617CgQb = TxNba1617CgQb.objects.all().values()
                try:
                    page = request.GET.get('page', 1)
                except PageNotAnInteger:
                    page = 1
                p = Paginator(tx1617CgQb, 50, request=request)
                tx1617CgQb = p.page(page)
                return render(request, 'data.html', {'tx1617CgCj': tx1617CgCj, 'tx1617CgQb': tx1617CgQb})
        elif nianfen == "1718":
            if saiji == "季前赛":
                tx1718JqCj = TxNba1718JqCj.objects.all().values()
                page = 1
                p = Paginator(tx1718JqCj, 50, request=request)
                tx1718JqCj = p.page(page)

                tx1718jqQb = TxNba1718JqQb.objects.all().values()
                try:
                    page = request.GET.get('page', 1)
                except PageNotAnInteger:
                    page = 1
                p = Paginator(tx1718jqQb, 50, request=request)
                tx1718jqQb = p.page(page)
                return render(request, 'data.html', {'tx1718JqCj': tx1718JqCj, 'tx1718jqQb': tx1718jqQb})
            elif saiji == "季后赛":
                tx1718JhCj = TxNba1718JhCj.objects.all().values()
                page = 1
                p = Paginator(tx1718JhCj, 50, request=request)
                tx1718JhCj = p.page(page)

                tx1718jhQb = TxNba1718JhQb.objects.all().values()
                try:
                    page = request.GET.get('page', 1)
                except PageNotAnInteger:
                    page = 1
                p = Paginator(tx1718jhQb, 50, request=request)
                tx1718jhQb = p.page(page)
                return render(request, 'data.html', {'tx1718JhCj': tx1718JhCj, 'tx1718jhQb': tx1718jhQb})
            elif saiji == "常规赛":
                tx1718CgCj = TxNba1718CgCj.objects.all().values()
                page = 1
                p = Paginator(tx1718CgCj, 50, request=request)
                tx1718CgCj = p.page(page)

                tx1718CgQb = TxNba1718CgQb.objects.all().values()
                try:
                    page = request.GET.get('page', 1)
                except PageNotAnInteger:
                    page = 1
                p = Paginator(tx1718CgQb, 50, request=request)
                tx1718CgQb = p.page(page)
                return render(request, 'data.html', {'tx1718CgCj': tx1718CgCj, 'tx1718CgQb': tx1718CgQb})

# 雷达图配置
def radar(index1,index2):
    from pyecharts import Radar
    ss = TxNba1718CgCj._meta.fields  #获取字段
    attr=[]
    for i in ss:
        if i.name == "defen_selected":
            q = ("场均得分",'100')
            attr.append(q)
        elif i.name == "zhugong":
            q = ("场均助攻", '20')
            attr.append(q)
        elif i.name == "qiangduan":
            q = ("场均抢断", '10')
            attr.append(q)
        elif i.name == "lanban":
            q = ("场均篮板", '30')
            attr.append(q)
        elif i.name == "gaimao":
            q = ("场均盖帽", '20')
            attr.append(q)

    v3 = [list(TxNba1718CgCj.objects.values('defen_selected','zhugong','qiangduan','lanban','gaimao')[index1].values())]
    v4 = [list(TxNba1718CgCj.objects.values('defen_selected', 'zhugong', 'qiangduan', 'lanban', 'gaimao')[index2].values())]
    # v3_name = [list(TxNba1718CgCj.objects.values("qiuyuan")[index1].values())]
    # v4_name = [list(TxNba1718CgCj.objects.values("qiuyuan")[index2].values())]
    radar = Radar()
    radar.config(attr)
    # radar.add(v3_name[0][0],v3,is_splitline_show=True,is_axisline_show=True,label_color=[],is_area_show=True)
    # radar.add(v4_name[0][0], v4, is_splitline_show=True, is_axisline_show=True,label_color=[],legend_selectedmode='single')

    radar.add("one",v3,is_splitline_show=True,is_axisline_show=True,label_color=[],is_area_show=True)
    radar.add("two", v4, is_splitline_show=True, is_axisline_show=True,label_color=[],legend_selectedmode='single')

    return radar


def tt():
    index1 = random.randint(1, 50)
    index2 = random.randint(1, 50)
    while index1 == index2:
        index2 = random.randint(1, 50)
    return  index1,index2

# 生成雷达图(启用配置)


class chartDisplayView(View):
    def get(self,request):
        template = loader.get_template('chart.html')
        index1,index2 = tt()

        b = radar(index1, index2)
        context = dict(
            myechart=b.render_embed(),
            host=REMOTE_HOST,
            script_list=b.get_js_dependencies()
        )
        return HttpResponse(template.render(context, request))

    def post(self,request):
        pass


# 随机匹配

class someMatchView(View):
    def get(self, request):
        return render(request,'data.html',{})

    def post(self, request):
        index1,index2 = tt()
        v_left = PlayerInfo.objects.all()[index2]
        v_right = PlayerInfo.objects.all()[index1]
        return render(request, 'data.html', {"v_left": v_left, "v_right": v_right})


class NoBackView(View):
    def get(self,request):
        return HttpResponse("暂未开放")

    def post(self,request):
        pass


class TestView(View):
    def get(self,request):
        return render(request,'setting_info.html',{})

    def post(self,request):
        pass

class saichengView(View):
    def get_time(self):
        now_time = datetime.datetime.now().date() #4

        forward_time = str(datetime.datetime.now().date())
        day1 = str(int(forward_time.split('-')[2])-1) # 1 2 3
        day2 = str(int(forward_time.split('-')[2])-2)  # 1 2 3
        if int(day1) <=10 :
            forward_time1 = forward_time.split('-')[0] + '-' + forward_time.split('-')[1] + '-' + '0' + day1
        else:
            forward_time1 = forward_time.split('-')[0] + '-' + forward_time.split('-')[1] + '-' + '1' + day1

        if int(day2) <=10:
            forward_time2 = forward_time.split('-')[0] + '-' + forward_time.split('-')[2] + '-' + '0' + day2
        else:
            forward_time2 = forward_time.split('-')[0] + '-' + forward_time.split('-')[2] + '-' + '1' + day2


        after_time = str(datetime.datetime.now().date())
        day4 = str(int(after_time.split('-')[2]) + 1)  # 1 2 3
        day5 = str(int(after_time.split('-')[2]) + 2)  # 1 2 3
        if int(day4) <= 10:
            after_time1 = after_time.split('-')[0] + '-' + after_time.split('-')[1] + '-' + '0' + day4
        else:
            after_time1 = after_time.split('-')[0] + '-' + after_time.split('-')[1] + '-' + '1' + day4

        if int(day5) <=10:
            after_time2 = after_time.split('-')[0] + '-' + after_time.split('-')[2] + '-' + '0' + day5
        else:
            after_time2 = after_time.split('-')[0] + '-' + after_time.split('-')[2] + '-' + '1' + day5

        return now_time, forward_time1, forward_time2,  after_time1, after_time2

    def get(self,request):
        now_time, forward_time1, forward_time2,  after_time1, after_time2= self.get_time()
        now_saicheng = Saicheng.objects.filter(datatime=now_time)
        forward_time1 = Saicheng.objects.filter(datatime=forward_time1)
        forward_time2 = Saicheng.objects.filter(datatime=forward_time2)
        after_time1 = Saicheng.objects.filter(datatime=after_time1)
        after_time2 = Saicheng.objects.filter(datatime=after_time2)
        return render(request,'saicheng.html',{'now_saicheng': now_saicheng, 'now_time': now_time,
                                               'forward_time1': forward_time1,'forward_time2': forward_time2, 'after_time1': after_time1,
                                               'after_time2': after_time2})

    def post(self,request):
        pass

