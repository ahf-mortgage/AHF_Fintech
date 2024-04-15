
from django.contrib import admin
from django.urls import path
from .views import home,change_branch_amount,loan_break_point



urlpatterns = [
    path('',home,name="home"),
    path('change_branch_amount/',change_branch_amount,name="change_branch_amount"),
    path('loan_break_point/',loan_break_point,name="loan_break_point"),
    
]