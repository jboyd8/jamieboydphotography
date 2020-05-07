from django.urls import path

from . import views

urlpatterns = [
    path('view_cart', views.view_cart, name='view_cart'),
    path('add/<int:blog_id>', views.add_to_cart, name='add_to_cart'),
    path('adjust/<int:blog_id>', views.adjust_cart, name='adjust_cart'),
]
