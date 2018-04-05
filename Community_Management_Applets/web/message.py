import json
from web.views import decodeToken
import logging
from web.models import User,Message


# 新建消息,request中提交 需要通知的人
def createMessage(request):
    pass


# 获取当前用户的信息数量
def getMessageCount(request):
    content = json.loads(request.body)
    openid = decodeToken(content['token'])

    logging.info("openid: " + openid + " get message count.")

    user = User.objects.get(openid=openid)
    count = user.message_set.count()
    return HttpResponse(count)

# 获取用户的所有消息
def getMessageUnread(request):
    content = json.loads(request.body)
    openid = decodeToken(content['token'])

    logging.info("openid: " + openid + " get unread messages.")

    user = User.objects.get(openid=openid)
    messagesJson = serializers.serialize("json",user.message_set.objects.all())
    return JsonResponse(messagesJson)