from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from recruiter.models import Bps,LoanBreakPoint,CompPlan,AHF,Branch
import math


@login_required
def home(request):
    bps              = Bps.objects.all().first()
    loan_break_point = LoanBreakPoint.objects.all().first()
    comp_plan        = CompPlan.objects.all().first()
    ahf              = AHF.objects.all().first() 
    branch           = Branch.objects.all().first() 
    gci               = bps.bps * loan_break_point.loan_break_point/10000 + comp_plan.Flat_Fee
    # ahf_commission    =    gci * ahf.commission # the percentage of ahf (30%)
    # amount ahf must get from gci = gci * 30 
    # they are two diffrent variables
    
    
    branch_commission = gci * float(branch.commission)
    ahf_commission = gci * (1 - float(branch.commission))
    ahf_amount =  100 - branch.commission * 100
    # print( 100 - branch.commission * 100)
    interval_bps = [num for num in range(50,275,25)]

    
    context = {
        'ahf_amount': math.ceil(ahf_amount) if ahf_amount > 0 else None,
        'interval_bps':interval_bps,
        'branch_amount': math.ceil(branch.commission * 100) if branch.commission > 0 else None,
        'bps':bps.bps if bps.bps > 0 else None,
        'loan_break_point': math.ceil(loan_break_point.loan_break_point) ,# if loan_break_point >0 else None,
        'comp_plan':comp_plan.Flat_Fee if comp_plan.Flat_Fee > 0 else None,
        'gci':math.ceil(gci) if gci > 0 else None,
        'ahf_commission': math.ceil(ahf_commission) if ahf_commission > 0 else None,
        'ahf_commission_amount':  1 - float(branch.commission) if branch.commission > 0 else None ,#ahf_amount, # ahf.commission,
        'branch_commission': math.ceil(branch_commission) if branch_commission > 0 else None,
        'branch_commission_amount':branch.commission if branch.commission > 0 else None

    }
    return render(request,"home/index2.html",context)