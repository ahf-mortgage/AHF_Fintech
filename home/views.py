from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from recruiter.models import Bps,LoanBreakPoint,CompPlan,AHF,Branch



@login_required
def home(request):
    bps              = Bps.objects.all().first()
    loan_break_point = LoanBreakPoint.objects.all().first()
    comp_plan        = CompPlan.objects.all().first()
    ahf              = AHF.objects.all().first() 
    branch           = Branch.objects.all().first()
    
    gci               = bps.bps * loan_break_point.loan_break_point/10000 + comp_plan.Flat_Fee
    ahf_commission    = gci * ahf.commission
    branch_commission = gci * branch.commission


    
    context = {
        'bps':bps.bps,
        'loan_break_point':loan_break_point.loan_break_point,
        'comp_plan':comp_plan.Flat_Fee,
        'gci':gci,
        'ahf_commission': ahf_commission,
        'ahf_commission_amount':ahf.commission,
        'branch_commission':branch_commission,
        'branch_commission_amount':branch.commission

    }
    return render(request,"home/index.html",context)