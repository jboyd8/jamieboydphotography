from django.urls import path

from . import views

urlpatterns = [
    path('landscapes', views.landscapes, name='landscapes'),
    path('portraits', views.portraits, name='portraits'),
    path('cityscapes', views.logout_cityscapes, name='cityscapes'),
]
