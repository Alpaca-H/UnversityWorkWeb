# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import datetime


class HupuNbaNews(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    img_url = models.CharField(max_length=255, blank=True, null=True)
    fabu_time = models.CharField(max_length=255, blank=True, null=True)
    context = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    forums_url = models.CharField(max_length=255, blank=True, null=True)
    comments = models.TextField(verbose_name="评论",max_length=225,null=True)

    class Meta:
        managed = False
        db_table = 'hupu_nba_news'
        verbose_name = "虎扑新闻"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class XlNews(models.Model):
    title = models.CharField(max_length=255,primary_key=True )
    detail_url = models.CharField(max_length=255, blank=True, null=True)
    title_time = models.CharField(max_length=255, blank=True, null=True)
    team_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xl_news'
        verbose_name = "新浪新闻"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ZbbNews(models.Model):
    title = models.CharField(primary_key=True, max_length=255)
    detail_url = models.CharField(max_length=255, blank=True, null=True)
    title_time = models.CharField(max_length=255, blank=True, null=True)
    team_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zbb_news'
        verbose_name = "直播吧新闻"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class TxVideo(models.Model):
    video_time = models.CharField(max_length=255, blank=True, null=True)
    video_id = models.CharField(max_length=255, blank=True, null=True)
    video_img = models.CharField(max_length=255, blank=True, null=True)
    video_playurl = models.CharField(db_column='video_playUrl', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    video_num = models.CharField(max_length=255, blank=True, null=True)
    video_title = models.CharField(primary_key=True, max_length=255)
    true_url = models.CharField(max_length=255, blank=True, null=True)
    video_theme = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tx_video'
        verbose_name = "腾讯视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.video_title


class Comments(models.Model):
    titleID = models.IntegerField(blank=True,null=True)
    level = models.IntegerField(blank=True,null=True)
    time = models.CharField(max_length=255,blank=True,null=True)
    comment = models.CharField(max_length=255,blank=True,null=True)

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.titleID


# 点赞模块
# 首先用户会在新闻浏览界面进行新闻内容的阅读，对于自己喜欢的内容，可以进行点赞
# 1.用户点赞  2.通过ajax记录当前文章的文章编号  3.存入数据库，并显示动画效果表明点赞成功
class UserParse(models.Model):
    """
    字段说明:
    1.titleid 记鹿当前点赞文章id
    2.parse_time 记录当前点赞的时间
    3.parse_user 记录当前点赞的用户
    4.is_parse  记录当前内容是否已经被点赞   (1)表示已经点赞 (2)表示已经取消点赞
    """
    titleid = models.IntegerField(default=100,verbose_name="文章id")
    parse_time = models.DateTimeField(default=datetime.datetime.now,verbose_name="点赞时间")
    parse_user = models.CharField(verbose_name="点赞用户",max_length=100)
    is_True = models.CharField(verbose_name="是否点赞",max_length=20)

    class Meta:
        verbose_name = "点赞模块"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.parse_user


class Saicheng(models.Model):
    datatime = models.CharField(max_length=255, blank=True, null=True)
    starttime = models.CharField(db_column='startTime', max_length=255, blank=True, null=True)
    matchname = models.CharField(db_column='matchName', max_length=255, blank=True, null=True)
    link = models.CharField(primary_key=True, max_length=255)
    leftlogo = models.CharField(db_column='leftLogo', max_length=255, blank=True, null=True)
    leftname = models.CharField(db_column='leftName', max_length=255, blank=True, null=True)
    rightlogo = models.CharField(db_column='rightLogo', max_length=255, blank=True, null=True)
    rightname = models.CharField(db_column='rightName', max_length=255, blank=True, null=True)
    vsline = models.CharField(db_column='VsLine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'saicheng'
        verbose_name = "赛程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.datatime