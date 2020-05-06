from django.urls import path

from . import views

urlpatterns = [
    path('<int:comment_id>', views.edit_comment, name='edit_comment'),
    path('<int:comment_id>/delete', views.delete_comment, name='delete_comment'),
]
