from django.contrib import admin
from django.urls import path
from . import views

app_name = 'catalog1'

urlpatterns = [    
    path('', views.IndexView.as_view(),name="index"),
]
