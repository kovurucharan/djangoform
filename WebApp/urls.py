from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('thank/',views.Thanks,name="thanks"),
    path('register/',views.Register,name="register"),

]