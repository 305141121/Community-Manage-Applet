from django.shortcuts import render

# Create your views here.

from django.http.response import HttpResponse
from django.http.request import HttpRequest
import requests
import json
import logging
import time
import jwt
from web.models import User

# 需要appid 和 appsecret 保持会话
appid = 'wx3e821923eeac1991'
appsecret = '0445508f47987667cb28446ed8886a13'

# 获取用户的openID，用于标识用户。若程序不单单依赖于小程序，还有其他平台的话，需要获取unionID
def index(request):
    if request.method == "GET":
        print("REQUEST!!!!")
        return HttpResponse("Test finish!!!")
    if request.method == "POST":
        reJson = json.loads(request.body)
        code = reJson['code']
        print("json:"+json.dumps(reJson))
        logging.info(request.body)

        url = 'https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code' % (
        appid, appsecret, code)

        re = requests.get(url)
        # result返回 session_key 和 openid
        reJson = json.loads(re.content.decode('utf-8'))
        openid = reJson['openid']
        logging.info("currentUser: "+openid)

        # 用户登入小程序即为其创建数据库记录
        # newUser = User(openid=openid)
        # newUser.save()

        # 加密openid
        token = createToken(openid)
        return HttpResponse(token)


# 更改用户信息,'POST'，上传信息时需要上传 token 标识用户
# name, phone, sex, grade, major
def updateUserInfo(request):
    logging.warning("updateUserInfo!!!")
    content = json.loads(request.body)
    openid = decodeToken(content['token'])


    logging.info("openid: "+openid)

    user = User.objects.get(openid=openid)


    logging.warning("User！！！！"+user.openid)
    print("content:\n"+str(content))
    print("user.name: "+user.name)
    user.name = content['name']
    user.save()
    print("user.NAME: "+user.name)
    user.phone = content['phone']
    user.sex = content['sex']
    user.grade = content['grade']
    user.major = content['major']
    user.save()

    logging.warning("save success!!")

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
    logging.warning("WARNNING:  "+token)
    payload = jwt.decode(token, key='secret', algorithms='HS256')
    return payload['openid']