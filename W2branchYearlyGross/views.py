
from django.shortcuts import render,redirect
from .models import BranchPayrollLiabilitiesQ, BranchPayrollLiabilitieR
from .forms import BranchPayrollLiabilitiesQForm

def control_Q_value_branch_payroll_liabilities(request):

    if request.method == "POST":
        Q_value = request.POST.get("Q_value")
        try:
            instance = BranchPayrollLiabilitiesQ.objects.get(Q_value = Q_value)
            if instance:
                instance.value = float(request.POST.get("value"))
                print("instance value ",instance.value, "request.POST.get('value') ",request.POST.get("value"))
                instance.save()
                return redirect("/")
            else:
                form = BranchPayrollLiabilitiesQForm(request.POST)
                print(form.errors," form errors",form.is_valid()," form status")
                if form.is_valid():
                    form.save()
                    return redirect("/")
        except Exception as e:
            raise e
  
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
  
        
        
