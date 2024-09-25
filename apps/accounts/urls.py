from django.contrib import admin
from django.urls import path,include
from .views import login_view,sign_up

urlpatterns = [
    path('login/',login_view,name = "login"),
    path('sign-up/',sign_up,name = "sign-up")

]
