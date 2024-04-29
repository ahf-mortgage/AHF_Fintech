
from django.contrib import admin
from django.urls import path
from .views import (
    control_Q_value_branch_payroll_liabilities,
    control_R_value_branch_payroll_liabilities,
    control_expense
    )


app_name = "W2branchYearlyGross"
urlpatterns = [
    path('q/',control_Q_value_branch_payroll_liabilities,name="control_Q_value_branch_payroll_liabilities"),
    path('r/',control_R_value_branch_payroll_liabilities,name="control_R_value_branch_payroll_liabilities"),
    path('control_expense/',control_expense,name="control_expense"),
    
]