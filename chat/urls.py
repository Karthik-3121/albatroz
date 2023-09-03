from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="messages"),
    path("search/", views.search, name="search"),
    path("addfriend/<str:username>", views.addFriend, name="addFriend"),
    path("chat/<str:username>", views.chat, name="chat"),
    path('api/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),
    path('api/', views.message_list, name='message-list'),
]