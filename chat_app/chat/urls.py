from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('login', views.login, name='login'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.get_messages, name='getMessages'),
    path('choose_room', views.choose_room, name='chooseroom')
]
