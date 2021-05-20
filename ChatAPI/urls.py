from django.urls import path
from ChatAPI import views

urlpatterns = [
    path('', views.Chat, name='home'),
    path('/chat', views.Chat, name='Chat'),
]
