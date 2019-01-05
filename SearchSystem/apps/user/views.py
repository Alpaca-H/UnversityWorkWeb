from django.shortcuts import render
# Create your views here.


from django.http import HttpResponse
from django.views.generic.base import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend  # 验证
from apps.user.models import Web_User, EamilVerifyRecord
from django.db.models import Q
from .forms import LoginForm, RegisterForm, ForgetForm
from django.contrib.auth import hashers  # 哈希加密
from utils.email_send import email_link_send
from news.models import Comments,UserParse
from datetime import datetime
import os
from SearchSystem import settings

# 验证类
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Web_User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as  e:
            return None


# 登陆类
class LoginView(View):
    def get(self, request):
        return render(request, 'first.html', {})

    def post(self, request):
        # 验证表单
        login_forms = LoginForm(request.POST)
        # 如果表单存在返回True
        if login_forms.is_valid():
            # 提取表单中的内容，Username以及password
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            # 调用Django内部函数验证，不存在则返回None
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                # 验证是否激活
                if user.is_active:
                    login(request, user)
                    return render(request, "zhnashi.html")
                # 未激活则返回信息
                else:
                    return render(request, "first.html", context={"msg": "用户未激活"})
            else:
                return render(request, "first.html", context={"msg": "用户名或密码错误"})
        else:
            return render(request, "first.html", context={"login_forms": login_forms})


# 注册类
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "zhuce.html", {"register_form": register_form})

    def post(self, request):
        # 获取注册表单对象
        register_form = RegisterForm(request.POST)
        # 验证注册表单格式
        if register_form.is_valid():
            # 获取表单内容
            email = request.POST.get("email", "")
            if Web_User.objects.filter(email=email):
                return render(request, "zhuce.html", {"msg": "用户已经存在"})
            password = request.POST.get("password", "")
            username = request.POST.get("username", "")
            # 获取数据库 对象
            user_web = Web_User()
            user_web.email = email
            user_web.password = password
            user_web.username = username
            user_web.is_active = False
            user_web.password = hashers.make_password(password)
            email_link_send(email, "register")
            user_web.save()
            return render(request, 'first.html', {})
        else:
            return render(request, 'zhuce.html', {"register_form": register_form})


#  忘记密码类
class NopasswordView(View):
    def get(self, request):
        forget_forms = ForgetForm()
        return render(request, "nopassword.html", {"forget_forms": forget_forms})

    def post(self, request):
        # 获取忘记密码表单对象
        forget_form = ForgetForm(request.POST)
        # 判断格式是否正确
        if forget_form.is_valid():
            email = request.POST.get("email", "")
            password = request.POST.get("password", "")
            user = Web_User.objects.get(email=email)
            if user:
                email_link_send(email, sent_type="forget")
                user.password = hashers.make_password(password)
                user.is_active = False
                user.save()
                # 修改密码之后 直接修改了原有的密码数据，但是会给与用于一个未激活的状态，需要用户跳转到邮箱的链接才可以验证
                return render(request, 'first.html', {})
            else:
                return render(request, 'nopassword.html', {'msg': "好像并没有这个用户"})


# 链接验证类
class ResgisterActiveView(View):
    # 链接跳转验证，提取数据库内容与Code比对
    # 匹配正确则返回True
    def get(self, request, code):
        all_records = EamilVerifyRecord.objects.filter(code=code)
        if all_records:
            for record in all_records:
                email = record.email
                user = Web_User.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return HttpResponse("用户不存在")
        return render(request, 'first.html', {})


# 修改密码类
class changePasswordView(View):
    # 修改密码类，提取数据库内内容
    # 与账号比对，如果账号存在且Code验证码为True 则保存
    def get(self, request, code):
        all_records = EamilVerifyRecord.objects.filter(code=code)
        if all_records:
            for record in all_records:
                email = record.email
                user = Web_User.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return HttpResponse("用户不存在")
        return render(request, 'first.html', {})


# 评论类
class CommentsView(View):
    def get(self, request):
        return render(request, 'first.html', {})

    def post(self, request):
        type = request.POST.get("type"," ")
        ttext = request.POST.get('ttext', " ")
        nickName = request.POST.get('nickName', " ")
        id = request.POST.get("id", "")
        time = datetime.now()
        text = nickName+":"+ttext
        if type == "ccet":
            level = 1
            Comments.objects.create(comment=text,titleID=id,time=time,level=level)
            data = 1
            return HttpResponse(data)
        elif type == "reply":
            level = 2
            Comments.objects.create(comment=text, titleID=id, time=time, level=level)
            data = 1
            return HttpResponse(data)


# 用户点赞
class UserParseView(View):
    def get(self, request):
        pass

    def post(self, request):
        D = request.POST.get("D"," ")
        titleid = request.POST.get("titleid" , " ")
        parse_user = request.POST.get("parse_user"," ")
        if D == "like":

            is_has = UserParse.objects.filter(titleid=titleid,parse_user=parse_user)
            if is_has.exists():
                is_has.is_True = 1
            else:
                 UserParse.objects.create(titleid=titleid,parse_user=parse_user,is_True=1)
            data = 1
            return HttpResponse(data)
        else:
            parseModel = UserParse.objects.get( titleid=titleid,parse_user=parse_user)
            parseModel.is_True = 2
            parseModel.save()
            data = 1
            return HttpResponse(data)

# 用户上传头像或者修改个人信息
class UserUploadSettingView(View):
    def get(self, request):
        pass

    def post(self, request):
        zhanghao = request.POST.get("zhanghao", " ")
        xingshi = request.POST.get("xingshi", " ")
        mingzi = request.POST.get("mingzi", " ")
        nicheng = request.POST.get("nicheng", " ")
        touxiang = request.FILES.get('touxiang',"1")
        Set_User = Web_User.objects.get(username=zhanghao)
        Set_User.last_name = xingshi
        Set_User.first_name = mingzi
        Set_User.nike_name = nicheng
        Set_User.head_image = touxiang
        Set_User.save()
        return render(request, 'setting_info.html')
