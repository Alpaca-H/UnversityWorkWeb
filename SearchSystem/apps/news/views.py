from django.shortcuts import render
from django.views import View
from .models import HupuNbaNews, XlNews, TxVideo, ZbbNews, Comments,UserParse

from pure_pagination.paginator import EmptyPage, Paginator, PageNotAnInteger


# Create your views here.


# 新闻展示页面 文字图片
class NewsDisplay(View):
    def get(self, request, type):
        if type == "hupu":
            news_dp = HupuNbaNews.objects.all().values()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(news_dp, 10, request=request)  # 表示每页的数量
        news_dp = p.page(page)
        userparse = UserParse.objects.all()
        return render(request, 'news.html', {'news_dp': news_dp,'userparse':userparse})

    def post(self, request):
        pass


# 新闻列表View  有评论
class NewsAllView(View):
    def get(self, request, id):
        news_list = HupuNbaNews.objects.get(id=id)
        comments = Comments.objects.filter(titleID=id)

        if comments:
            comments = comments
            return render(request, "news_deatil.html",{"news_list": news_list, "id": id, "comments": comments})
        else:
            NoneComments = "暂时还没有任何评论"
            return render(request, "news_deatil.html", {"news_list": news_list, "id": id, "NoneComments": NoneComments})

    def post(self, request):
        pass


# 新闻列表View  文字
class NewsListView(View):
    def get(self, request):
        news_list_10 = HupuNbaNews.objects.all()[:10]
        news_list_20 = HupuNbaNews.objects.all()[10:20]
        news_list_30 = HupuNbaNews.objects.all()[20:30]
        xl_news_list_10 = XlNews.objects.all()[:10]
        xl_news_list_20 = XlNews.objects.all()[10:20]
        xl_news_list_30 = XlNews.objects.all()[20:30]
        zbb_news_list_10 = ZbbNews.objects.all()[:10]
        zbb_news_list_20 = ZbbNews.objects.all()[10:20]
        zbb_news_list_30 = ZbbNews.objects.all()[20:30]

        return render(request, "newsList.html", {
            "hupu_news_10": news_list_10, "hupu_news_20": news_list_20, "hupu_news_30": news_list_30,
            "xl_news_list_10": xl_news_list_10, "xl_news_list_20": xl_news_list_20, "xl_news_list_30": xl_news_list_30,
            "zbb_news_list_10": zbb_news_list_10, "zbb_news_list_20": zbb_news_list_20,
            "zbb_news_list_30": zbb_news_list_30,
        })

    def post(self, request):
        pass


# 视频View
class Top100View(View):
    def get(self, request):
        top_list = TxVideo.objects.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(top_list, 24, request=request)  # 表示每页的数量
        top_list = p.page(page)
        return render(request, "Top100.html", {'topLists': top_list})

    def post(self, request):
        pass


