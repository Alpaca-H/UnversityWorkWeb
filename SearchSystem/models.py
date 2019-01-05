# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Saicheng(models.Model):
    datatime = models.CharField(max_length=255, blank=True, null=True)
    starttime = models.CharField(db_column='startTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    matchname = models.CharField(db_column='matchName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    link = models.CharField(primary_key=True, max_length=255)
    leftlogo = models.CharField(db_column='leftLogo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    leftname = models.CharField(db_column='leftName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rightlogo = models.CharField(db_column='rightLogo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rightname = models.CharField(db_column='rightName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vsline = models.CharField(db_column='VsLine', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'saicheng'
