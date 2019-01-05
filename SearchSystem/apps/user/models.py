from django.db import models
from django.contrib.auth.models import  AbstractUser  #继承自带的User表
# Create your models here.

import  datetime

class Web_User(AbstractUser):
    nike_name = models.CharField(max_length=50,default="小明",verbose_name="昵称",)  #昵称
    # is_active =  是否是激活的
    # is_staff =  是否是职工
    # is_superuser = 是否是超级管理员
    mobile = models.CharField(max_length=13,null=True,blank=True,verbose_name="手机号码")  #手机号码
    # null = true  数据库字段可以是空的
    # blank = true 输入框内可以是空的
    birth_day = models.DateField(verbose_name="出生日期",null=True,blank=True); #出生日期
    head_image = models.ImageField(upload_to="image/%Y/%m",default="image/default.png",max_length=200,verbose_name="用户头像") #用户头像
    mail = models.EmailField(max_length=20,verbose_name="邮箱",null=True,blank=True)  #邮箱
    sex = models.CharField(choices=(("male","男"),("female","女"),("it","其他")),default="female",verbose_name="性别",max_length=10)
    # user_id = models.IntegerField(verbose_name="用户序号")
    # random = models.CharField(verbose_name="用户序号",max_length=10)
    limit = models.CharField(verbose_name="用户权限",choices=(("T1","管理员"),("T2","会员用户"),("T3","特权用户"),("Tothers","免费用户")\
                                                          ),default="T1",max_length=10)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


# 数据库设计说明，在这个项目中我们会有访问用户的表即Web_User表，同时还会有其他类型的表
# 因此在调用的过程中很容易出现死循环
# 于是我们要产生一个高于这些表的Operation表来管理这些散开的表
# 比如用户的点赞收藏等操作，会凌驾于user以及news等内容，这个时候我们就会容易出错


# 注册需要的邮箱验证码
class EamilVerifyRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name="验证码")
    email = models.EmailField(max_length=50,verbose_name="邮箱")
    send_type = models.CharField(choices=(("register","注册"),("forget","忘记密码")),max_length=20,verbose_name="验证码类型")
    send_time = models.DateTimeField(default=datetime.datetime.now,verbose_name="发送时间")
    # 这里对datetime.now()做一个解释，如果是datetime.datetime.now()则是根据这个class类编译的时间创建
    # 而如果是datetime.now则是根据创建这个实例的时候的时间

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email

# 首页的轮播图
class Banner(models.Model):
    title = models.CharField(verbose_name="标题",max_length=20)
    image = models.ImageField(upload_to="banner/%Y/%m",verbose_name="轮播图",max_length=100)
    url = models.URLField(max_length=200,verbose_name="访问地址")
    index = models.IntegerField(default=100,verbose_name="顺序")
    add_time = models.DateTimeField(default=datetime.datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class MeseageSetting(models.Model):
    Mes_txt = models.CharField(verbose_name="消息内容",max_length=200)
    Mes_User = models.CharField(verbose_name="消息对象",max_length=20)
    Mes_time = models.DateTimeField(verbose_name="消息时间",max_length=20)
    is_read = models.IntegerField(verbose_name="是否已经阅读")

    class Meta:
        verbose_name = "站内信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Mes_txt