from django.urls import path
from ChatAPI import views

urlpatterns = [
    path('', views.api_Overview, name='home'),
    path('chat/', views.Chat_, name='Chat Post'),
    path('chat/<str:pattern>/', views.Chat, name='Chat Get'),
    # path('tags/', views.Tags, name='Chat Tags'),

]
