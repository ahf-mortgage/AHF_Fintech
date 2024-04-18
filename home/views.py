from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from recruiter.models import Bps,LoanBreakPoint,CompPlan,AHF,Branch
import math
from  django.shortcuts import redirect


# @login_required
def home(request):
    """
        This function display comp plan,loan above limit and loan below limit
    """
    bps              = Bps.objects.all().first()
    loan_break_point = LoanBreakPoint.objects.all().first()
    comp_plan        = CompPlan.objects.all().first()
    ahf              = AHF.objects.all().first() 
    branch           = Branch.objects.all().first() 
    gci               = (comp_plan.Percentage * 100) * loan_break_point.loan_break_point/10000 + comp_plan.Flat_Fee
    
    
    
    branch_commission = gci * float(branch.commission)
    ahf_commission = gci * (1 - float(branch.commission))
    ahf_amount =  100 - branch.commission * 100
    
    
    
    min_loan = 100000 
    rows = [50] +  [num for num in range(100,275,25)]
    row_counter = [i-7 for i in range(7,7+ len(rows))]
    print(row_counter ," row_counter")
    print("DEBUG rows ",rows)
    loan_below_limits = [num for num in range(int(loan_break_point.loan_break_point),min_loan - min_loan,-min_loan)]
    
    

    gci = (comp_plan.Percentage * 100) * loan_break_point.loan_break_point / 10000 + comp_plan.Flat_Fee
    if gci > comp_plan.MAX_GCI:
        gci = comp_plan.MAX_GCI
    FLAT_AM0UNT = gci - (gci/1000) * ((loan_below_limits[len(loan_below_limits) - 1] or 0) * 0.1/10000) 
    
 
    context = {
        'loan_below_limits':loan_below_limits,
        'comp_plan_for_lower_limit':comp_plan,
        'ahf_amount': math.ceil(ahf_amount) if ahf_amount > 0 else None,
        'rows':rows,
        'branch_amount': math.ceil(branch.commission * 100) if branch.commission > 0 else None,
        'bps':bps.bps if bps.bps > 0 else None,
        'loan_break_point': math.ceil(loan_break_point.loan_break_point) ,# if loan_break_point >0 else None,
        'comp_plan':comp_plan.Flat_Fee if comp_plan.Flat_Fee > 0 else None,
        'gci': math.ceil(gci),
        'ahf_commission': math.ceil(ahf_commission) if ahf_commission > 0 else None,
        'ahf_commission_amount':  1 - float(branch.commission) if branch.commission > 0 else None ,#ahf_amount, # ahf.commission,
        'branch_commission': math.ceil(branch_commission) if branch_commission > 0 else None,
        'branch_commission_amount':branch.commission if branch.commission > 0 else None

    }
    return render(request,"home/index2.html",context)





# toggle a branch amout 
def change_branch_amount(request):
    branch = Branch.objects.all().first()
   
    if request.method == "POST":
        branch_amount = request.POST.get("branch_amount")
        branch_amount = int(branch_amount) / 100
        branch.commission = branch_amount
        branch.save()
        return redirect("/")
    
    context = {
        
    }
    return render(request,"home/index2.html",context)


# toggle a comp plan gci max
def change_comp_plan_max_gci(request):
    comp_plan = CompPlan.objects.all().first()
   
    if request.method == "POST":
        max_gci = request.POST.get('max_gci',None)
        comp_plan.MAX_GCI = max_gci
        comp_plan.save()
       
        return redirect("/")
    
    context = {
        
    }
    return render(request,"home/index2.html",context)




# toggle a comp plan
def change_comp_plan(request):
    comp_plan_obj = CompPlan.objects.all().first()
    if request.method == "POST":
        comp_plan = request.POST.get("comp_plan")
        print("comp plan ",comp_plan)
        comp_plan_obj.Percentage = comp_plan
        comp_plan_obj.save()
        return redirect("/")
    
    context = {
        
    }
    return render(request,"home/index2.html",context)



def loan_break_point(request):
    loan_break_point = LoanBreakPoint.objects.all().first()
    


    if request.method == "POST":
        loan_break= request.POST.get("loan_break_point")
        loan_break_point.loan_break_point = int(loan_break)
        loan_break_point.save()
        return redirect("/")
    
    context = {
        
    }
    return render(request,"home/index2.html",context)


def comp_plan_change_view(request):
    """
        This function handle comp plane changes

    """
    
    
    loan_break_point = LoanBreakPoint.objects.all().first()
    comp_plan_obj = CompPlan.objects.all().first()
    branch = Branch.objects.all().first()

    if request.method == "POST":
        max_gci = request.POST.get('max_gci',None)
        comp_plan = request.POST.get("comp_plan")
        loan_break= request.POST.get("loan_break_point")
        branch_amount = request.POST.get("branch_amount")
        
        if True:
            comp_plan_obj.MAX_GCI = max_gci
            comp_plan_obj.Percentage = float(comp_plan)
            loan_break_point.loan_break_point = int(loan_break)
            branch_amount = int(branch_amount) / 100
            branch.commission = branch_amount
            branch.save()
            loan_break_point.save()
            comp_plan_obj.save()
            return redirect("/")
            
        else:
            return redirect("/")
            
                


      
    
    context = {
        
    }
    return render(request,"home/index2.html",context)