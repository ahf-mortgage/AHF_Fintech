
from django.contrib import admin
from django.urls import path
from .views import (
    control_Q_value_branch_payroll_liabilities,
    control_R_value_branch_payroll_liabilities,
    control_Q_value_for_employee_with_holding,
    control_expense,
    control_Q22_value
    )



app_name = "W2branchYearlyGross"
urlpatterns = [
    path('q/',control_Q_value_branch_payroll_liabilities,name="control_Q_value_branch_payroll_liabilities"),
    path('r/',control_R_value_branch_payroll_liabilities,name="control_R_value_branch_payroll_liabilities"),
    path('control_expense/',control_expense,name="control_expense"),
    path('control_Q22_value/',control_Q22_value,name="control_Q22_value"),
    path('control_Q_value_for_employee_with_holding/',control_Q_value_for_employee_with_holding,name="control_Q_value_for_employee_with_holding")
    
]