
from django.contrib import admin
from django.urls import path
from .views import home,change_branch_amount,loan_break_point,change_comp_plan,change_comp_plan_max_gci



urlpatterns = [
    path('',home,name="home"),
    path('change_branch_amount/',change_branch_amount,name="change_branch_amount"),
    path('change_comp_plan/',change_comp_plan,name="change_comp_plan"),
    path('loan_break_point/',loan_break_point,name="loan_break_point"),
    path('change_comp_plan_max_gci/',change_comp_plan_max_gci,name = "change_comp_plan_max_gci")
    
]