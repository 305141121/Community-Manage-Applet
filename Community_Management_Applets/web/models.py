# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activity(models.Model):
    activityid = models.IntegerField(db_column='activityId', primary_key=True)  # Field name made lowercase.
    activityurl = models.CharField(db_column='activityUrl', max_length=256)  # Field name made lowercase.
    msgtitle = models.CharField(db_column='msgTitle', max_length=32, blank=True, null=True)  # Field name made lowercase.
    msgcdnurl = models.CharField(db_column='msgCdnUrl', max_length=256, blank=True, null=True)  # Field name made lowercase.
    community_comid = models.ForeignKey('Community', models.DO_NOTHING, db_column='community_comId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'activity'


class Community(models.Model):
    communityid = models.CharField(db_column='communityId', primary_key=True, max_length=45)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=32)
    intro = models.CharField(max_length=256)
    logo = models.TextField()

    class Meta:
        managed = False
        db_table = 'community'


class CommunityHasUser(models.Model):
    community_comid = models.ForeignKey(Community, models.DO_NOTHING, db_column='community_comId', primary_key=True)  # Field name made lowercase.
    user_openid = models.ForeignKey('User', models.DO_NOTHING, db_column='user_openid')
    role = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'community_has_user'
        unique_together = (('community_comid', 'user_openid'),)


class Message(models.Model):
    messageid = models.CharField(db_column='messageId', primary_key=True, max_length=45)  # Field name made lowercase.
    content = models.CharField(max_length=256)
    readed = models.IntegerField()
    sendtime = models.DateField()
    user_openid = models.ForeignKey('User', models.DO_NOTHING, db_column='user_openid')

    class Meta:
        managed = False
        db_table = 'message'


class User(models.Model):
    openid = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=32, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    grade = models.SmallIntegerField(blank=True, null=True)
    major = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
