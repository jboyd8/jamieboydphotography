from django.urls import path

from . import views

urlpatterns = [
    path('blogs', views.blogs, name='blogs'),
    path('<int:blog_id>', views.blog, name='blog'),
]
