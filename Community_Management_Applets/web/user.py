from django.shortcuts import render

# Create your views here.

from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.http import JsonResponse
import requests
import json
import logging
import time
import jwt
from web.models import User,Message
from django.core import serializers

logger = logging.getLogger('django')

# 需要appid 和 appsecret 保持会话
appid = 'wx3e821923eeac1991'
appsecret = '0445508f47987667cb28446ed8886a13'
# appid = 'wxa87c214527bc82c5'
# appsecret = '309bb222b1c61ec156af70b092f3f6ac'
# 获取用户的openID，用于标识用户。若程序不单单依赖于小程序，还有其他平台的话，需要获取unionID
def login(request):

        reJson = json.loads(request.body)
        code = reJson['code']

        url = 'https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code' % (
        appid, appsecret, code)

        re = requests.get(url)
        # result返回 session_key 和 openid
        reJson = json.loads(re.content.decode('utf-8'))
        print(re.content.decode('utf-8'))
        openid = reJson['openid']

        logger.info("User: "+openid+" login.")

        # 用户初次登入小程序即为其创建数据库记录
        if not User.objects.filter(openid=openid):
            newUser = User(openid=openid)
            logger.info(openid+" create new user")
            newUser.save()

        # 加密openid
        token = createToken(openid)
        return HttpResponse(token)


# 获取用户信息, 小程序端需要解析以下字段获取对应内容
def getUserInfo(request):
    content = json.loads(request.body)
    openid = decodeToken(content['token'])

    logger.info("openid: " + openid + " get information.")
    user = User.objects.filter(openid=openid)

    jsondata = {}
    jsondata['name']=user[0].name
    jsondata['sex']=user[0].sex
    jsondata['grade']=user[0].grade
    jsondata['major']=user[0].major
    jsondata['phone']=user[0].phone

    return JsonResponse(jsondata)


# 更改用户信息,'POST'，上传信息时需要上传 token 标识用户
# name, phone, sex, grade, major
def updateUserInfo(request):
    content = json.loads(request.body)
    openid = decodeToken(content['token'])

    logger.info("openid: "+openid+" update information.")

    user = User.objects.get(openid=openid)
    user.name = content['name']
    user.phone = content['phone']
    user.sex = content['sex']
    user.grade = content['grade']
    user.major = content['major']
    user.save()
    return HttpResponse("success")


# 通过 jwt 加密并通过openid标识用户
def createToken(openid):
    payload = {
        "openid": openid
    }
    token = jwt.encode(payload=payload,key='secret',algorithm='HS256')
    return token


# jwt解密获得用户的openid
def decodeToken(token):
    payload = jwt.decode(token, key='secret', algorithms='HS256')
    return payload['openid']


