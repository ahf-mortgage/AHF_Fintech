from django.contrib import admin
from django.urls import path
from .views import MloOnboardingView


app_name = "home"
urlpatterns = [
    path('',MloOnboardingView.as_view(),name="home"),
   
    
]