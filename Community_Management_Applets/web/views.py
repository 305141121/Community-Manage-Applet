from django.shortcuts import render

# Create your views here.

from django.http.response import HttpResponse
from django.http.request import HttpRequest
import requests
import json
import logging
import time
import jwt


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
        result = re.content

        print(result)

        return HttpResponse("cool")


# 更改用户信息,'POST'
def updateInfo(request):
    content = json.load(request.body)


# 通过 jwt 标识用户维持登录态
def createToken():
    payload = {
        # token 过期时间为 2小时
        "exp": int(time.time())+7200
    }
