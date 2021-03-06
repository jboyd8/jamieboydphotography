from django.urls import path

from . import views

urlpatterns = [
    path('view_cart', views.view_cart, name='view_cart'),
    path('add/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('adjust/<str:id>', views.adjust_cart, name='adjust_cart'),
]
