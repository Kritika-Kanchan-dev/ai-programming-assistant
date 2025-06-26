from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_view, name='chat'),
    path('delete/<int:chat_id>/', views.delete_chat, name='delete_chat'),
    path('clear/', views.clear_chats, name='clear_chats'),
]
