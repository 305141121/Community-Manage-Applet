from django.urls import path
from web import views

urlpatterns = [
    path('', views.index)
    path('updateInfo/', views.updateInfo)
]