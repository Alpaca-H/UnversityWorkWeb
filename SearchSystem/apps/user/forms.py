# -*- coding:utf-8 -*-
__author__ = 'hzj'


from django import forms
from captcha.fields import CaptchaField

#登录表单
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    #requird =True  必须填写的字段
    #form表单这里可以做验证.同字段一样
    #因此就可以做手机啊 邮箱啊之类的验证了。
    password = forms.CharField(required=True,min_length=5)



#注册表单
class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=5)
    username = forms.CharField(min_length=6,required=True,error_messages={"username_invalid":"用户名错误"})
    captcha = CaptchaField(error_messages={"invalid":"验证码错误"}) #验证码字段

#忘记密码表单
class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=5)


# 评论表单
class CommentsForm(forms.Form):
    comments_text = forms.CharField(required=True, min_length=5, max_length=200)






