
from django.contrib import admin
from django.urls import path
from apps.recruiter.views import (
    change_branch_amount,
    loan_break_point,
    change_comp_plan,
    change_comp_plan_max_gci,
    comp_plan_change_view,
    change_branch_loan,
    change_ahf_loan
    )
from apps.home.views import home
from apps.RevenueShare.views import visualize_graph

app_name = "home"
urlpatterns = [
    path('',home,name="home"),
    path('change_branch_amount/',change_branch_amount,name="change_branch_amount"),
    # path('change_comp_plan/',change_comp_plan,name="change_comp_plan"),
    path('loan_break_point/',loan_break_point,name="loan_break_point"),
    path('visualize_map/',visualize_graph,name="visualize_graph"),
    path('change_branch_loan/',change_branch_loan,name="change_branch_loan"),
    path('change_ahf_loan/',change_ahf_loan,name="change_ahf_loan"),
    path('comp_plan_change_view/',comp_plan_change_view,name="comp_plan_change_view"),
    path('change_comp_plan_max_gci/',change_comp_plan_max_gci,name = "change_comp_plan_max_gci")
    
]