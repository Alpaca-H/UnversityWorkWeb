# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

#1718常规场均
class TxNba1718CgCj(models.Model):
    paiming = models.CharField(max_length=255, blank=True, null=True)
    qiuyuan = models.CharField(max_length=255, blank=True, null=True)
    qiudui = models.CharField(max_length=255, blank=True, null=True)
    defen_selected = models.CharField(max_length=255, blank=True, null=True)
    chushou = models.CharField(max_length=255, blank=True, null=True)
    mingzhong = models.CharField(max_length=255, blank=True, null=True)
    chushou3 = models.CharField(max_length=255, blank=True, null=True)
    mingzhong3 = models.CharField(max_length=255, blank=True, null=True)
    faci = models.CharField(max_length=255, blank=True, null=True)
    falv = models.CharField(max_length=255, blank=True, null=True)
    lanban = models.CharField(max_length=255, blank=True, null=True)
    qlanban = models.CharField(max_length=255, blank=True, null=True)
    hlanban = models.CharField(max_length=255, blank=True, null=True)
    zhugong = models.CharField(max_length=255, blank=True, null=True)
    qiangduan = models.CharField(max_length=255, blank=True, null=True)
    gaimao = models.CharField(max_length=255, blank=True, null=True)
    shiwu = models.CharField(max_length=255, blank=True, null=True)
    fangui = models.CharField(max_length=255, blank=True, null=True)
    changci = models.CharField(max_length=255, blank=True, null=True)
    shangchang = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Tx_nba_1718_cg_cj'

#1718常规全部
class TxNba1718CgQb(models.Model):
    paiming = models.CharField(max_length=255, blank=True, null=True)
    qiuyuan = models.CharField(max_length=255, blank=True, null=True)
    qiudui = models.CharField(max_length=255, blank=True, null=True)
    defen_selected = models.CharField(max_length=255, blank=True, null=True)
    chushou = models.CharField(max_length=255, blank=True, null=True)
    mingzhong = models.CharField(max_length=255, blank=True, null=True)
    chushou3 = models.CharField(max_length=255, blank=True, null=True)
    mingzhong3 = models.CharField(max_length=255, blank=True, null=True)
    faci = models.CharField(max_length=255, blank=True, null=True)
    falv = models.CharField(max_length=255, blank=True, null=True)
    lanban = models.CharField(max_length=255, blank=True, null=True)
    qlanban = models.CharField(max_length=255, blank=True, null=True)
    hlanban = models.CharField(max_length=255, blank=True, null=True)
    zhugong = models.CharField(max_length=255, blank=True, null=True)
    qiangduan = models.CharField(max_length=255, blank=True, null=True)
    gaimao = models.CharField(max_length=255, blank=True, null=True)
    shiwu = models.CharField(max_length=255, blank=True, null=True)
    fangui = models.CharField(max_length=255, blank=True, null=True)
    changci = models.CharField(max_length=255, blank=True, null=True)
    shangchang = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Tx_nba_1718_cg_qb'

#1718季后场均
class TxNba1718JhCj(models.Model):
    paiming = models.CharField(max_length=255, blank=True, null=True)
    qiuyuan = models.CharField(max_length=255, blank=True, null=True)
    qiudui = models.CharField(max_length=255, blank=True, null=True)
    defen_selected = models.CharField(max_length=255, blank=True, null=True)
    chushou = models.CharField(max_length=255, blank=True, null=True)
    mingzhong = models.CharField(max_length=255, blank=True, null=True)
    chushou3 = models.CharField(max_length=255, blank=True, null=True)
    mingzhong3 = models.CharField(max_length=255, blank=True, null=True)
    faci = models.CharField(max_length=255, blank=True, null=True)
    falv = models.CharField(max_length=255, blank=True, null=True)
    lanban = models.CharField(max_length=255, blank=True, null=True)
    qlanban = models.CharField(max_length=255, blank=True, null=True)
    hlanban = models.CharField(max_length=255, blank=True, null=True)
    zhugong = models.CharField(max_length=255, blank=True, null=True)
    qiangduan = models.CharField(max_length=255, blank=True, null=True)
    gaimao = models.CharField(max_length=255, blank=True, null=True)
    shiwu = models.CharField(max_length=255, blank=True, null=True)
    fangui = models.CharField(max_length=255, blank=True, null=True)
    changci = models.CharField(max_length=255, blank=True, null=True)
    shangchang = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Tx_nba_1718_jh_cj'

#1718季后前部
class TxNba1718JhQb(models.Model):
    paiming = models.CharField(max_length=255, blank=True, null=True)
    qiuyuan = models.CharField(max_length=255, blank=True, null=True)
    qiudui = models.CharField(max_length=255, blank=True, null=True)
    defen_selected = models.CharField(max_length=255, blank=True, null=True)
    chushou = models.CharField(max_length=255, blank=True, null=True)
    mingzhong = models.CharField(max_length=255, blank=True, null=True)
    chushou3 = models.CharField(max_length=255, blank=True, null=True)
    mingzhong3 = models.CharField(max_length=255, blank=True, null=True)
    faci = models.CharField(max_length=255, blank=True, null=True)
    falv = models.CharField(max_length=255, blank=True, null=True)
    lanban = models.CharField(max_length=255, blank=True, null=True)
    qlanban = models.CharField(max_length=255, blank=True, null=True)
    hlanban = models.CharField(max_length=255, blank=True, null=True)
    zhugong = models.CharField(max_length=255, blank=True, null=True)
    qiangduan = models.CharField(max_length=255, blank=True, null=True)
    gaimao = models.CharField(max_length=255, blank=True, null=True)
    shiwu = models.CharField(max_length=255, blank=True, null=True)
    fangui = models.CharField(max_length=255, blank=True, null=True)
    changci = models.CharField(max_length=255, blank=True, null=True)
    shangchang = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Tx_nba_1718_jh_qb'

# 1718季后场均
class TxNba1718JqCj(models.Model):
    paiming = models.CharField(max_length=255, blank=True, null=True)
    qiuyuan = models.CharField(max_length=255, blank=True, null=True)
    qiudui = models.CharField(max_length=255, blank=True, null=True)
    defen_selected = models.CharField(max_length=255, blank=True, null=True)
    chushou = models.CharField(max_length=255, blank=True, null=True)
    mingzhong = models.CharField(max_length=255, blank=True, null=True)
    chushou3 = models.CharField(max_length=255, blank=True, null=True)
    mingzhong3 = models.CharField(max_length=255, blank=True, null=True)
    faci = models.CharField(max_length=255, blank=True, null=True)
    falv = models.CharField(max_length=255, blank=True, null=True)
    lanban = models.CharField(max_length=255, blank=True, null=True)
    qlanban = models.CharField(max_length=255, blank=True, null=True)
    hlanban = models.CharField(max_length=255, blank=True, null=True)
    zhugong = models.CharField(max_length=255, blank=True, null=True)
    qiangduan = models.CharField(max_length=255, blank=True, null=True)
    gaimao = models.CharField(max_length=255, blank=True, null=True)
    shiwu = models.CharField(max_length=255, blank=True, null=True)
    fangui = models.CharField(max_length=255, blank=True, null=True)
    changci = models.CharField(max_length=255, blank=True, null=True)
    shangchang = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Tx_nba_1718_jq_cj'

# 1718季后场均
class TxNba1718JqQb(models.Model):
    paiming = models.CharField(max_length=255, blank=True, null=True)
    qiuyuan = models.CharField(max_length=255, blank=True, null=True)
    qiudui = models.CharField(max_length=255, blank=True, null=True)
    defen_selected = models.CharField(max_length=255, blank=True, null=True)
    chushou = models.CharField(max_length=255, blank=True, null=True)
    mingzhong = models.CharField(max_length=255, blank=True, null=True)
    chushou3 = models.CharField(max_length=255, blank=True, null=True)
    mingzhong3 = models.CharField(max_length=255, blank=True, null=True)
    faci = models.CharField(max_length=255, blank=True, null=True)
    falv = models.CharField(max_length=255, blank=True, null=True)
    lanban = models.CharField(max_length=255, blank=True, null=True)
    qlanban = models.CharField(max_length=255, blank=True, null=True)
    hlanban = models.CharField(max_length=255, blank=True, null=True)
    zhugong = models.CharField(max_length=255, blank=True, null=True)
    qiangduan = models.CharField(max_length=255, blank=True, null=True)
    gaimao = models.CharField(max_length=255, blank=True, null=True)
    shiwu = models.CharField(max_length=255, blank=True, null=True)
    fangui = models.CharField(max_length=255, blank=True, null=True)
    changci = models.CharField(max_length=255, blank=True, null=True)
    shangchang = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Tx_nba_1718_jq_qb'

class TxNba1516CgCj(models.Model):
    paiming = models.CharField(max_length=255, blank=True, null=True)
    qiuyuan = models.CharField(max_length=255, blank=True, null=True)
    qiudui = models.CharField(max_length=255, blank=True, null=True)
    defen_selected = models.CharField(max_length=255, blank=True, null=True)
    chushou = models.CharField(max_length=255, blank=True, null=True)
    mingzhong = models.CharField(max_length=255, blank=True, null=True)
    chushou3 = models.CharField(max_length=255, blank=True, null=True)
    mingzhong3 = models.CharField(max_length=255, blank=True, null=True)
    faci = models.CharField(max_length=255, blank=True, null=True)
    falv = models.CharField(max_length=255, blank=True, null=True)
    lanban = models.CharField(max_length=255, blank=True, null=True)
    qlanban = models.CharField(max_length=255, blank=True, null=True)
    hlanban = models.CharField(max_length=255, blank=True, null=True)
    zhugong = models.CharField(max_length=255, blank=True, null=True)
    qiangduan = models.CharField(max_length=255, blank=True, null=True)
    gaimao = models.CharField(max_length=255, blank=True, null=True)
    shiwu = models.CharField(max_length=255, blank=True, null=True)
    fangui = models.CharField(max_length=255, blank=True, null=True)
    changci = models.CharField(max_length=255, blank=True, null=True)
    shangchang = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'Tx_nba_1516_cg_cj'

class TxNba1516CgQb(models.Model):
    paiming = models.CharField(max_length=255, blank=True, null=True)
    qiuyuan = models.CharField(max_length=255, blank=True, null=True)
    qiudui = models.CharField(max_length=255, blank=True, null=True)
    defen_selected = models.CharField(max_length=255, blank=True, null=True)
    chushou = models.CharField(max_length=255, blank=True, null=True)
    mingzhong = models.CharField(max_length=255, blank=True, null=True)
    chushou3 = models.CharField(max_length=255, blank=True, null=True)
    mingzhong3 = models.CharField(max_length=255, blank=True, null=True)
    faci = models.CharField(max_length=255, blank=True, null=True)
    falv = models.CharField(max_length=255, blank=True, null=True)
    lanban = models.CharField(max_length=255, blank=True, null=True)
    qlanban = models.CharField(max_length=255, blank=True, null=True)
    hlanban = models.CharField(max_length=255, blank=True, null=True)
    zhugong = models.CharField(max_length=255, blank=True, null=True)
    qiangduan = models.CharField(max_length=255, blank=True, null=True)
    gaimao = models.CharField(max_length=255, blank=True, null=True)
    shiwu = models.CharField(max_length=255, blank=True, null=True)
    fangui = models.CharField(max_length=255, blank=True, null=True)
    changci = models.CharField(max_length=255, blank=True, null=True)
    shangchang = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Tx_nba_1516_cg_qb'

class TxNba1516JqCj(models.Model):
    paiming = models.CharField(max_length=255, blank=True, null=True)
    qiuyuan = models.CharField(max_length=255, blank=True, null=True)
    qiudui = models.CharField(max_length=255, blank=True, null=True)
    defen_selected = models.CharField(max_length=255, blank=True, null=True)
    chushou = models.CharField(max_length=255, blank=True, null=True)
    mingzhong = models.CharField(max_length=255, blank=True, null=True)
    chushou3 = models.CharField(max_length=255, blank=True, null=True)
    mingzhong3 = models.CharField(max_length=255, blank=True, null=True)
    faci = models.CharField(max_length=255, blank=True, null=True)
    falv = models.CharField(max_length=255, blank=True, null=True)
    lanban = models.CharField(max_length=255, blank=True, null=True)
    qlanban = models.CharField(max_length=255, blank=True, null=True)
    hlanban = models.CharField(max_length=255, blank=True, null=True)
    zhugong = models.CharField(max_length=255, blank=True, null=True)
    qiangduan = models.CharField(max_length=255, blank=True, null=True)
    gaimao = models.CharField(max_length=255, blank=True, null=True)
    shiwu = models.CharField(max_length=255, blank=True, null=True)
    fangui = models.CharField(max_length=255, blank=True, null=True)
    changci = models.CharField(max_length=255, blank=True, null=True)
    shangchang = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'Tx_nba_1516_jq_cj'

class TxNba1516JqQb(models.Model):
    paiming = models.CharField(max_length=255, blank=True, null=True)
    qiuyuan = models.CharField(max_length=255, blank=True, null=True)
    qiudui = models.CharField(max_length=255, blank=True, null=True)
    defen_selected = models.CharField(max_length=255, blank=True, null=True)
    chushou = models.CharField(max_length=255, blank=True, null=True)
    mingzhong = models.CharField(max_length=255, blank=True, null=True)
    chushou3 = models.CharField(max_length=255, blank=True, null=True)
    mingzhong3 = models.CharField(max_length=255, blank=True, null=True)
    faci = models.CharField(max_length=255, blank=True, null=True)
    falv = models.CharField(max_length=255, blank=True, null=True)
    lanban = models.CharField(max_length=255, blank=True, null=True)
    qlanban = models.CharField(max_length=255, blank=True, null=True)
    hlanban = models.CharField(max_length=255, blank=True, null=True)
    zhugong = models.CharField(max_length=255, blank=True, null=True)
    qiangduan = models.CharField(max_length=255, blank=True, null=True)
    gaimao = models.CharField(max_length=255, blank=True, null=True)
    shiwu = models.CharField(max_length=255, blank=True, null=True)
    fangui = models.CharField(max_length=255, blank=True, null=True)
    changci = models.CharField(max_length=255, blank=True, null=True)
    shangchang = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Tx_nba_1516_jq_qb'

class TxNba1516JhQb(models.Model):
    paiming = models.CharField(max_length=255, blank=True, null=True)
    qiuyuan = models.CharField(max_length=255, blank=True, null=True)
    qiudui = models.CharField(max_length=255, blank=True, null=True)
    defen_selected = models.CharField(max_length=255, blank=True, null=True)
    chushou = models.CharField(max_length=255, blank=True, null=True)
    mingzhong = models.CharField(max_length=255, blank=True, null=True)
    chushou3 = models.CharField(max_length=255, blank=True, null=True)
    mingzhong3 = models.CharField(max_length=255, blank=True, null=True)
    faci = models.CharField(max_length=255, blank=True, null=True)
    falv = models.CharField(max_length=255, blank=True, null=True)
    lanban = models.CharField(max_length=255, blank=True, null=True)
    qlanban = models.CharField(max_length=255, blank=True, null=True)
    hlanban = models.CharField(max_length=255, blank=True, null=True)
    zhugong = models.CharField(max_length=255, blank=True, null=True)
    qiangduan = models.CharField(max_length=255, blank=True, null=True)
    gaimao = models.CharField(max_length=255, blank=True, null=True)
    shiwu = models.CharField(max_length=255, blank=True, null=True)
    fangui = models.CharField(max_length=255, blank=True, null=True)
    changci = models.CharField(max_length=255, blank=True, null=True)
    shangchang = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'Tx_nba_1516_jh_qb'

class TxNba1516JhCj(models.Model):
    paiming = models.CharField(max_length=255, blank=True, null=True)
    qiuyuan = models.CharField(max_length=255, blank=True, null=True)
    qiudui = models.CharField(max_length=255, blank=True, null=True)
    defen_selected = models.CharField(max_length=255, blank=True, null=True)
    chushou = models.CharField(max_length=255, blank=True, null=True)
    mingzhong = models.CharField(max_length=255, blank=True, null=True)
    chushou3 = models.CharField(max_length=255, blank=True, null=True)
    mingzhong3 = models.CharField(max_length=255, blank=True, null=True)
    faci = models.CharField(max_length=255, blank=True, null=True)
    falv = models.CharField(max_length=255, blank=True, null=True)
    lanban = models.CharField(max_length=255, blank=True, null=True)
    qlanban = models.CharField(max_length=255, blank=True, null=True)
    hlanban = models.CharField(max_length=255, blank=True, null=True)
    zhugong = models.CharField(max_length=255, blank=True, null=True)
    qiangduan = models.CharField(max_length=255, blank=True, null=True)
    gaimao = models.CharField(max_length=255, blank=True, null=True)
    shiwu = models.CharField(max_length=255, blank=True, null=True)
    fangui = models.CharField(max_length=255, blank=True, null=True)
    changci = models.CharField(max_length=255, blank=True, null=True)
    shangchang = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'Tx_nba_1516_jh_cj'


#---------1617----------
class TxNba1617JhCj(models.Model):
    paiming = models.CharField(max_length=255, blank=True, null=True)
    qiuyuan = models.CharField(max_length=255, blank=True, null=True)
    qiudui = models.CharField(max_length=255, blank=True, null=True)
    defen_selected = models.CharField(max_length=255, blank=True, null=True)
    chushou = models.CharField(max_length=255, blank=True, null=True)
    mingzhong = models.CharField(max_length=255, blank=True, null=True)
    chushou3 = models.CharField(max_length=255, blank=True, null=True)
    mingzhong3 = models.CharField(max_length=255, blank=True, null=True)
    faci = models.CharField(max_length=255, blank=True, null=True)
    falv = models.CharField(max_length=255, blank=True, null=True)
    lanban = models.CharField(max_length=255, blank=True, null=True)
    qlanban = models.CharField(max_length=255, blank=True, null=True)
    hlanban = models.CharField(max_length=255, blank=True, null=True)
    zhugong = models.CharField(max_length=255, blank=True, null=True)
    qiangduan = models.CharField(max_length=255, blank=True, null=True)
    gaimao = models.CharField(max_length=255, blank=True, null=True)
    shiwu = models.CharField(max_length=255, blank=True, null=True)
    fangui = models.CharField(max_length=255, blank=True, null=True)
    changci = models.CharField(max_length=255, blank=True, null=True)
    shangchang = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'Tx_nba_1617_jh_cj'


class TxNba1617JhQb(models.Model):
    paiming = models.CharField(max_length=255, blank=True, null=True)
    qiuyuan = models.CharField(max_length=255, blank=True, null=True)
    qiudui = models.CharField(max_length=255, blank=True, null=True)
    defen_selected = models.CharField(max_length=255, blank=True, null=True)
    chushou = models.CharField(max_length=255, blank=True, null=True)
    mingzhong = models.CharField(max_length=255, blank=True, null=True)
    chushou3 = models.CharField(max_length=255, blank=True, null=True)
    mingzhong3 = models.CharField(max_length=255, blank=True, null=True)
    faci = models.CharField(max_length=255, blank=True, null=True)
    falv = models.CharField(max_length=255, blank=True, null=True)
    lanban = models.CharField(max_length=255, blank=True, null=True)
    qlanban = models.CharField(max_length=255, blank=True, null=True)
    hlanban = models.CharField(max_length=255, blank=True, null=True)
    zhugong = models.CharField(max_length=255, blank=True, null=True)
    qiangduan = models.CharField(max_length=255, blank=True, null=True)
    gaimao = models.CharField(max_length=255, blank=True, null=True)
    shiwu = models.CharField(max_length=255, blank=True, null=True)
    fangui = models.CharField(max_length=255, blank=True, null=True)
    changci = models.CharField(max_length=255, blank=True, null=True)
    shangchang = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Tx_nba_1617_jh_qb'

class TxNba1617JqQb(models.Model):
    paiming = models.CharField(max_length=255, blank=True, null=True)
    qiuyuan = models.CharField(max_length=255, blank=True, null=True)
    qiudui = models.CharField(max_length=255, blank=True, null=True)
    defen_selected = models.CharField(max_length=255, blank=True, null=True)
    chushou = models.CharField(max_length=255, blank=True, null=True)
    mingzhong = models.CharField(max_length=255, blank=True, null=True)
    chushou3 = models.CharField(max_length=255, blank=True, null=True)
    mingzhong3 = models.CharField(max_length=255, blank=True, null=True)
    faci = models.CharField(max_length=255, blank=True, null=True)
    falv = models.CharField(max_length=255, blank=True, null=True)
    lanban = models.CharField(max_length=255, blank=True, null=True)
    qlanban = models.CharField(max_length=255, blank=True, null=True)
    hlanban = models.CharField(max_length=255, blank=True, null=True)
    zhugong = models.CharField(max_length=255, blank=True, null=True)
    qiangduan = models.CharField(max_length=255, blank=True, null=True)
    gaimao = models.CharField(max_length=255, blank=True, null=True)
    shiwu = models.CharField(max_length=255, blank=True, null=True)
    fangui = models.CharField(max_length=255, blank=True, null=True)
    changci = models.CharField(max_length=255, blank=True, null=True)
    shangchang = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'Tx_nba_1617_jq_qb'


class TxNba1617JqCj(models.Model):
    paiming = models.CharField(max_length=255, blank=True, null=True)
    qiuyuan = models.CharField(max_length=255, blank=True, null=True)
    qiudui = models.CharField(max_length=255, blank=True, null=True)
    defen_selected = models.CharField(max_length=255, blank=True, null=True)
    chushou = models.CharField(max_length=255, blank=True, null=True)
    mingzhong = models.CharField(max_length=255, blank=True, null=True)
    chushou3 = models.CharField(max_length=255, blank=True, null=True)
    mingzhong3 = models.CharField(max_length=255, blank=True, null=True)
    faci = models.CharField(max_length=255, blank=True, null=True)
    falv = models.CharField(max_length=255, blank=True, null=True)
    lanban = models.CharField(max_length=255, blank=True, null=True)
    qlanban = models.CharField(max_length=255, blank=True, null=True)
    hlanban = models.CharField(max_length=255, blank=True, null=True)
    zhugong = models.CharField(max_length=255, blank=True, null=True)
    qiangduan = models.CharField(max_length=255, blank=True, null=True)
    gaimao = models.CharField(max_length=255, blank=True, null=True)
    shiwu = models.CharField(max_length=255, blank=True, null=True)
    fangui = models.CharField(max_length=255, blank=True, null=True)
    changci = models.CharField(max_length=255, blank=True, null=True)
    shangchang = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'Tx_nba_1617_jq_cj'
class TxNba1617CgCj(models.Model):
    paiming = models.CharField(max_length=255, blank=True, null=True)
    qiuyuan = models.CharField(max_length=255, blank=True, null=True)
    qiudui = models.CharField(max_length=255, blank=True, null=True)
    defen_selected = models.CharField(max_length=255, blank=True, null=True)
    chushou = models.CharField(max_length=255, blank=True, null=True)
    mingzhong = models.CharField(max_length=255, blank=True, null=True)
    chushou3 = models.CharField(max_length=255, blank=True, null=True)
    mingzhong3 = models.CharField(max_length=255, blank=True, null=True)
    faci = models.CharField(max_length=255, blank=True, null=True)
    falv = models.CharField(max_length=255, blank=True, null=True)
    lanban = models.CharField(max_length=255, blank=True, null=True)
    qlanban = models.CharField(max_length=255, blank=True, null=True)
    hlanban = models.CharField(max_length=255, blank=True, null=True)
    zhugong = models.CharField(max_length=255, blank=True, null=True)
    qiangduan = models.CharField(max_length=255, blank=True, null=True)
    gaimao = models.CharField(max_length=255, blank=True, null=True)
    shiwu = models.CharField(max_length=255, blank=True, null=True)
    fangui = models.CharField(max_length=255, blank=True, null=True)
    changci = models.CharField(max_length=255, blank=True, null=True)
    shangchang = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'Tx_nba_1617_cg_cj'

class TxNba1617CgQb(models.Model):
    paiming = models.CharField(max_length=255, blank=True, null=True)
    qiuyuan = models.CharField(max_length=255, blank=True, null=True)
    qiudui = models.CharField(max_length=255, blank=True, null=True)
    defen_selected = models.CharField(max_length=255, blank=True, null=True)
    chushou = models.CharField(max_length=255, blank=True, null=True)
    mingzhong = models.CharField(max_length=255, blank=True, null=True)
    chushou3 = models.CharField(max_length=255, blank=True, null=True)
    mingzhong3 = models.CharField(max_length=255, blank=True, null=True)
    faci = models.CharField(max_length=255, blank=True, null=True)
    falv = models.CharField(max_length=255, blank=True, null=True)
    lanban = models.CharField(max_length=255, blank=True, null=True)
    qlanban = models.CharField(max_length=255, blank=True, null=True)
    hlanban = models.CharField(max_length=255, blank=True, null=True)
    zhugong = models.CharField(max_length=255, blank=True, null=True)
    qiangduan = models.CharField(max_length=255, blank=True, null=True)
    gaimao = models.CharField(max_length=255, blank=True, null=True)
    shiwu = models.CharField(max_length=255, blank=True, null=True)
    fangui = models.CharField(max_length=255, blank=True, null=True)
    changci = models.CharField(max_length=255, blank=True, null=True)
    shangchang = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Tx_nba_1617_cg_qb'



class PlayerInfo(models.Model):
    team_img = models.CharField(max_length=255, blank=True, null=True)
    start_urls = models.CharField(max_length=255, blank=True, null=True)
    imgurl = models.CharField(max_length=255, blank=True, null=True)
    c_name = models.CharField(primary_key=True, max_length=255)
    e_name = models.CharField(max_length=255)
    player_number = models.CharField(max_length=255, blank=True, null=True)
    weizhi = models.CharField(max_length=255, blank=True, null=True)
    shengao = models.CharField(max_length=255, blank=True, null=True)
    tizhong = models.CharField(max_length=255, blank=True, null=True)
    shengri = models.CharField(max_length=255, blank=True, null=True)
    hetong = models.CharField(max_length=255, blank=True, null=True)
    hetong2 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'player_info'




