from django.urls import path

from . import views

urlpatters = [
    path('', views.new_user_menu),
]