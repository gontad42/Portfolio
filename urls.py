from django.contrib import admin
from django.urls import path , include
from folio import views


urlpatterns = [
    path("", views.Inicio )
]
