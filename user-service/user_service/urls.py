from django.urls import path
from . import views

urlpatterns = [
    path('users', views.users, name='users'),
    path('users/<int:id>', views.user_detail, name='user_detail'),
]