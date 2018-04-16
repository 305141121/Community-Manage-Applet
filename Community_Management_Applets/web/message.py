import json

from django.http import HttpResponse, JsonResponse
from django.core import serializers
from web.user import decodeToken
import logging
from web.models import User, Message
from django.utils import dateformat
logger = logging.getLogger('django')

# 新建消息,request中提交 需要通知的人
def createMessage(request):
    pass


# 获取当前用户的信息数量
def getMessageCount(request):
    content = json.loads(request.body)
    openid = decodeToken(content['token'])

    logger.info("openid: " + openid + " get message count.")

    user = User.objects.get(openid=openid)
    count = user.message_set.filter(readed=0).count()
    return HttpResponse(count)

# 获取用户的所有消息
def getMessageUnread(request):
    content = json.loads(request.body)
    openid = decodeToken(content['token'])

    user = User.objects.get(openid=openid)

    logger.info("openid: " + openid + " get all message.")

    messages = user.message_set.filter(readed=0)

    messageJson = []
    # messageJson.append({"count":messages.count()})
    for mes in messages:
        mJson = {}
        mJson["content"] = mes.content
        mJson["sendtime"] = dateformat.format(mes.sendtime,'Y-m-d')
        messageJson.append(mJson)
    print(messageJson)

    # 标准json中使用双引号而不是单引号
    return HttpResponse(str(messageJson).replace('\'','\"'))


