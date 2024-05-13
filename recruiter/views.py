from django.shortcuts import render
from .models import MLO,Company,Loan
from django.shortcuts import get_object_or_404,redirect
from recruiter.models import Bps,LoanBreakPoint,CompPlan,AHF,Branch


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


def comp_plan_change_view(request):
    """
        This function handle comp plane changes

    """
    
    
    loan_break_point = LoanBreakPoint.objects.all().first()
    comp_plan_obj = CompPlan.objects.all().first()
    branch = Branch.objects.all().first()
    
   

    if request.method == "POST":
        Maximum_Compensation = request.POST.get("Maximum_Compensation",None)
        max_gci = request.POST.get('max_gci',None)
        comp_plan = request.POST.get("comp_plan")
        loan_break= request.POST.get("loan_break_point",0)
        branch_amount = request.POST.get("branch_amount")
        # CURRENT_Maximum_Compensation = comp_plan_obj.Maximum_Compensation
        
        if branch_amount != None:
            branch_amount = float(branch_amount)
            if branch_amount > 99:
                branch_amount = 99
     
        # if max_gci != None and Maximum_Compensation != None:
        if float(max_gci) > float(Maximum_Compensation):
            max_gci = Maximum_Compensation
        
        if branch_amount:
            comp_plan_obj.MAX_GCI             = max_gci
            comp_plan_obj.Maximum_Compensation    = float(Maximum_Compensation)
            comp_plan_obj.Percentage          = float(comp_plan)
            loan_break_point.loan_break_point = loan_break
            branch_amount                     = int(branch_amount) / 100
            branch.commission                 = branch_amount
            branch.save()
            loan_break_point.save()
            comp_plan_obj.save()
            return redirect("/")   
        else:
            return redirect("/")
  
    context = {
        
    }
    return render(request,"home/index2.html",context)

def change_branch_loan(request):
    if request.method == "POST":
        
        loan = Branch.objects.all().first()
        loan.loan_per_year = int(request.POST.get("M9"))
        loan.save()
        return  redirect("/")
    context = {
        
    }
    return render(request,"home/index2.html",context)


def change_ahf_loan(request):
    if request.method == "POST":
        loan = AHF.objects.all().first()
        loan.loan_per_year = int(request.POST.get("H10"))
        loan.save()
        return  redirect("/")
    context = {
        
    }
    return render(request,"home/index2.html",context)
    









# Create your views here.
# above 1,000,000
#   1,000,0000(loan to borrower) * 0.0275(comp 2.75%) = 27,500   <-- gci 


#  27,500 * 0.2(20% goes to company) = 5,500  
# 27,500 * 0.8(80% goes to ML0) = 22,000

#   5,500(compnay makes in one loan) * 32(number of loans) = 176,000(company makes this much,cap)

#   176,000 / 0.2 = 880,000  <--- 100% commision  20 goes to company and 80 goes to MLO


# loan_amount * 0.0275 = GCI <-- company gets 20% of this much

# example loan_amount = 500,000 ,then 500,000 * 0.0275 = 13,750(gci)
# 13,750(gci) * 0.2 = 2,750   <-- comission company gets
# 
# loan amount = 400,000 * 0.0275 = 11,000(gci)
# 11,000 * 0.2 = 2,200 <- commision company get

# (5,500 + 2,570 + 2,200 )= 10,270 (total company income)? > = 176,000 ==> 100% * gci to MLO else MLO gets 0.8 * gci 

# if total_company_income < 176000(cap):
# 	then: 
# 		company_get = 20 * gci;
# 	else:
# 		company_get = 0
# 		mlo_get = 100% * gci



# branch example
# from column L to O need to be tabulated in web
# variables 
# m3 = $L$23
# L23 = 02
# 02 = 1000000(input variables)
# loan_amount(l23) = 02

# k8 = sheet1(b32)
# sheet(b32) = Revenue Share Capped'!J11
# Revenue Share Capped'!J11 = =H11/2
# H11 = G8*G11
# G8 = =G9/20%
