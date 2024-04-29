
from django.shortcuts import render,redirect
from .models import BranchPayrollLiabilitieQ, BranchPayrollLiabilitieR
from .forms import BranchPayrollLiabilitiesQForm

def control_Q_value_branch_payroll_liabilities(request):
    instance = None
    try:
        instance = BranchPayrollLiabilitieQ.objects.all().first()
    except BranchPayrollLiabilitieQ.DoesNotExist as e:
        raise e

    if request.method == "POST":
        column_name = request.POST.get('column')
        value = request.POST.get('value')
        print("column name ",column_name,"value ",value)
        setattr(instance,column_name,value)
        instance.save()
        print("setattr(instance,column_name,value) ",setattr(instance,column_name,value))
        return redirect("/")
  
    return redirect("/")
  
  
  
  
  
  
def control_R_value_branch_payroll_liabilities(request):
    instance = None
    try:
        instance = BranchPayrollLiabilitieR.objects.all().first()
    except BranchPayrollLiabilitieR.DoesNotExist as e:
        raise e

    if request.method == "POST":
        column_name = request.POST.get('column')
        value = request.POST.get('value')
        print("column name ",column_name,"value ",value)
        setattr(instance,column_name,value)
        instance.save()
        print("setattr(instance,column_name,value) ",setattr(instance,column_name,value))
        return redirect("/")
  
    return redirect("/")
  
        
        
