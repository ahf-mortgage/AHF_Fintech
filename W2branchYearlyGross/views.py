
from django.shortcuts import render,redirect
from .models import BranchPayrollLiabilitiesQ
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
  
        
