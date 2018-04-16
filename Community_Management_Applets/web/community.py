
from web.models import Community,CommunityHasUser,User
from web.user import decodeToken
import json


# # 返回社团成员的粗略信息，返回json数据展示在成员列表栏
# def getCommunityMembers(request):
#     content = json.loads(request.body)
#     openid = decodeToken(content['token'])
#     communityId = content['communityId']
#
#     CommunityHasUser.objects.filter(communityId=communityId)
#
#     json = serializers.serialize("json",)
