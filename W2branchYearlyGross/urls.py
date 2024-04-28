
from django.contrib import admin
from django.urls import path
from .views import (
    control_Q_value_branch_payroll_liabilities
    )


app_name = "W2branchYearlyGross"
urlpatterns = [
    path('',control_Q_value_branch_payroll_liabilities,name="control_Q_value_branch_payroll_liabilities"),
    
]