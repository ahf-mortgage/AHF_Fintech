from django.contrib import admin
from django.urls import path
from . import views


app_name = "RevenueShare"
urlpatterns = [
    path('',views.revenue_view,name="revenue_view"),
    
]