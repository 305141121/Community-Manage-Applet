from django.urls import path
from web import views

urlpatterns = [
    path('index/', views.index),
    path('updateUserInfo/', views.updateUserInfo)
]