from django.urls import path
from web import user
from web import message
urlpatterns = [
    path('login/', user.login),
    path('updateUserInfo/', user.updateUserInfo),
    path('getUserInfo/', user.getUserInfo),

    path('getMessageUnread/', message.getMessageUnread),
    path('getMessageCount/', message.getMessageCount)
]

# path('getMessageCount/',message.getMessageCount)