
from django.shortcuts import render,redirect
from .models import (
    BranchPayrollLiabilitieQ,
    BranchPayrollLiabilitieR,
    EmployeeWithholdingQ,
    Category,
    Expense,
    Q22
    )

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
        setattr(instance,column_name,value)
        instance.save()
        return redirect("/")
  
    return redirect("/")


def control_Q_value_for_employee_with_holding(request):
    instance = None
    try:
        instance = EmployeeWithholdingQ.objects.all().first()
    except EmployeeWithholdingQ.DoesNotExist as e:
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






def control_expense(request):
    
    """
        Education and training
        Licensing fees
        Advertising & Marketing
    """
    category = Category.objects.all()
    expense = Expense.objects.all()
    if request.method == "POST":
        category_name = request.POST.get('category')
        expense_name  = request.POST.get('expense')
        category_expense = request.POST.get('category_expense')
        try:
            category = Category.objects.filter(name = category_name).first()
            expense = Expense.objects.filter(category = category ,name = expense_name).first()
        except Category.DoesNotExist or Expense.DoesNotExist:
            raise ValueError("not found")
        expense.expense = float(category_expense)
        expense.save()
        
        return redirect("/")
    return redirect("/")
  
  
  
def control_Q22_value(request):
    
    """
        control percentage to calculate W2 Taxable gross payroll
     
    """
    instance = Q22.objects.all().first()
    if request.method == "POST":
        q22 = request.POST.get("Q22")
        instance.value = q22
        instance.save()
        return redirect("/")
        
   
    return redirect("/")
  
        
  
        
        
