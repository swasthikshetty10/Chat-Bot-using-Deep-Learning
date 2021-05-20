from django.urls import path
from ChatAPI import views

urlpatterns = [
     path('', views.apiOverview, name='home'),
]