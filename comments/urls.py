from django.urls import path

from . import views

urlpatterns = [
    path('<int:comment_id>', views.edit_comment, name='edit_comment'),
]