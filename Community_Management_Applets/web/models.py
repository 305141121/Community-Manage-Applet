# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Community(models.Model):
    com_id = models.CharField(primary_key=True, max_length=45)
    name = models.CharField(unique=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'community'
        unique_together = (('com_id', 'name'),)


class CommunityHasUser(models.Model):
    community_com = models.ForeignKey(Community, models.DO_NOTHING, primary_key=True)
    user_wechat = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'community_has_user'
        unique_together = (('community_com', 'user_wechat'),)


class Message(models.Model):
    message_id = models.CharField(primary_key=True, max_length=45)
    content = models.CharField(max_length=256)
    user_wechat = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'message'


class User(models.Model):
    wechat_id = models.CharField(primary_key=True, max_length=16)
    name = models.CharField(max_length=32, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    major = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
