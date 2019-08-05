from django.urls import path, include
from RESTAPI import views

urlpatterns = [
    path('', views.index),
]
