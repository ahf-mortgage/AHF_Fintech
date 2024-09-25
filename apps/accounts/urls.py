from django.contrib import admin
from django.urls import path,include
from .views import login_view,sign_up,logout_view

urlpatterns = [
    path('login/',login_view,name = "login"),
    path('sign-up/',sign_up,name = "sign-up"),
    path('logout_view/',sign_up,name = "log-out")

]
