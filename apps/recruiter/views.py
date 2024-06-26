from django.shortcuts import render
from .models import MLO,Company,Loan
from django.shortcuts import get_object_or_404,redirect
from .models import Bps,LoanBreakPoint,CompPlan,AHF,Branch
from utils.calc_res import get_gci_result



def calculate_commission_above_million(loan_id,mlo_id):
	loan = None
	mlo = None
	gci = 0
	comp = 0
	split = 0.8

	try:
		loan = Loan.objects.get(id = loan_id)
	except Exception as e:
		raise e


	mlo = get_object_or_404(MLO,id = mlo_id)
	comp = mlo.comp


	if comp and loan:
		gci = loan.amount * comp
		mlo.MLO_commision += (split) * gci
		comp.COMPANY_commission += (1-split) * gci


	return mlo,company



def calculate_commission(loan_id,mlo_id,company_id):
	loan = None
	mlo = None
	company = None
	gci = 0
	comp = 0
	split = 0.8

	try:
		loan = Loan.objects.get(id = loan_id)
	except Exception as e:
		raise e


	mlo = get_object_or_404(MLO,id = mlo_id)
	company = get_object_or_404(Company,id = company_id )
	comp = mlo.comp
	gci = loan.amount * comp

	if company.total < company.cap:
		company.COMPANY_commission += (1 - split) * gci
	else:
		mlo.MLO_commision += gci
	return mlo



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

# from home.views import loan_below_limits
def comp_plan_change_view(request):
    """
        This function handle comp plane changes
        
        Flat_Fee=max_gci*loan_below_limits[len(loan_below_limits) -1]/10000

    """
    
    
    loan_break_point = LoanBreakPoint.objects.all().first()
    comp_plan_obj = CompPlan.objects.all().first()
    branch = Branch.objects.all().first()
    
   

    if request.method == "POST":
        Maximum_Compensation = request.POST.get("Maximum_Compensation",None)
        max_gci = request.POST.get('max_gci',None)
        FF_MIN_LOAN = request.POST.get('FF_MIN_LOAN',None)
        comp_plan = request.POST.get("comp_plan")
        loan_break= request.POST.get("loan_break_point",0)
        branch_amount = request.POST.get("branch_amount")
        
        if branch_amount != None:
            branch_amount = float(branch_amount)
            if branch_amount > 99:
                branch_amount = 99
     
        MIN_LOAN               =  100000 
        bps                    =  Bps.objects.all().first()
        rows                   = [50] +  [num for num in range(100,275,25)]
        row_counter            = [i-7 for i in range(7,7+ len(rows))]
        
        
        loan_below_limits      = [num for num in range(int(loan_break_point.loan_break_point),MIN_LOAN - MIN_LOAN,-MIN_LOAN)]  
        gci_result             = [(comp_plan_obj.Percentage * 100) * num / 10000 for num in range(int(loan_break_point.loan_break_point),MIN_LOAN - MIN_LOAN,-MIN_LOAN)]
        peak_loan_below_limits = loan_below_limits[len(loan_below_limits) - 1]
        peak_gci_results       = gci_result[len(gci_result)-1]        
        Flat_Fee               = comp_plan_obj.FF_MIN_LOAN - ((comp_plan_obj.Percentage * peak_loan_below_limits)/100)
   
        if float(max_gci) > float(Maximum_Compensation):
            max_gci = Maximum_Compensation
                     
        if FF_MIN_LOAN != None:
            comp_plan_obj.FF_MIN_LOAN = float(FF_MIN_LOAN)
            comp_plan_obj.save()
            
        
        if branch_amount:
            comp_plan_obj.FF_MIN_LOAN         = float(FF_MIN_LOAN)
            comp_plan_obj.MAX_GCI             = max_gci
            comp_plan_obj.Maximum_Compensation= float(Maximum_Compensation)
            comp_plan_obj.Flat_Fee            = Flat_Fee
            comp_plan_obj.Percentage          = float(comp_plan)
            loan_break_point.loan_break_point = loan_break
            branch_amount                     = int(branch_amount) / 100
            branch.commission                 = branch_amount
            bps.bps                           = float(comp_plan) * 100
            bps.save()
            loan_break_point.save()
            comp_plan_obj.save()
            branch.save()
            return redirect("/")   
        else:
            return redirect("/")
  
    context = {
        
    }
    return render(request,"home/entry.html",context)

def change_branch_loan(request):
    if request.method == "POST":
        
        loan = Branch.objects.all().first()
        loan.loan_per_year = int(request.POST.get("M9"))
        loan.save()
        return  redirect("/")
    context = {
        
    }
    return render(request,"home/entry.html",context)


def change_ahf_loan(request):
    if request.method == "POST":
        loan = AHF.objects.all().first()
        loan.loan_per_year = int(request.POST.get("H10"))
        loan.save()
        return  redirect("/")
    context = {
        
    }
    return render(request,"home/entry.html",context)
    


