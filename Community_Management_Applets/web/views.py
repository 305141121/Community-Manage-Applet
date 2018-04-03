from django.shortcuts import render

# Create your views here.

from django.http.response import HttpResponse
from django.http.request import HttpRequest
import requests
import json
import logging

# 需要appid 和 appsecret 保持会话
appid = 'wx3e821923eeac1991'
appsecret = '0445508f47987667cb28446ed8886a13'


def index(request):
    if request.method == "GET":
        print("REQUEST!!!!")
        return HttpResponse("Test finish!!!")
    if request.method == "POST":
        reJson = json.loads(request.body)
        code = reJson['code']

        logging.info(request.body)

        url = 'https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code' % (
        appid, appsecret, code)

        re = requests.get(url)
        result = re.content


        return HttpResponse("cool")