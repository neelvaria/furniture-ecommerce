from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.aboutpage, name='about'),
    path('shop/', views.shoppage, name='shop'),
]
