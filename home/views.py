from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from recruiter.models import Bps,LoanBreakPoint,CompPlan,AHF,Branch
import math
from  django.shortcuts import redirect
from utils.calc_res import (
                    calculate_annual_ahf_income,
                    calculate_gross_ahf_income,
                    gross_ahf_income,
                    branch_gross_income,
                    get_gci_result,
                    calculate_social_security,
                    calculate_total_expense,
                    calculate_medicare,
                    calculate_fed_un_employ,
                    calculate_CA_Unemployment

    )

from utils.w2_branch import W2_branch_column_names
from W2branchYearlyGross.models import (
                                        Category,
                                        EmployeeWithholding,
                                        BranchPayrollLiabilities,
                                        BranchPayrollLiabilitiesQ,
                                       BranchPayrollLiabilitieR
                                
                                        )





def home(request):
    """
        This function display comp plan,loan above limit and loan below limit
    """
    bps              = Bps.objects.all().first()
    loan_break_point = LoanBreakPoint.objects.all().first()
    comp_plan        = CompPlan.objects.all().first()
    ahf              = AHF.objects.all().first() 
    branch           = Branch.objects.all().first() 
    gci              = (comp_plan.Percentage * 100) * loan_break_point.loan_break_point/10000  #+ comp_plan.Flat_Fee
    
    
    
    branch_commission = gci * float(branch.commission)
    ahf_commission = gci * (1 - float(branch.commission))
    ahf_amount =  100 - branch.commission * 100
    
    
    
    min_loan = 100000 
    rows = [50] +  [num for num in range(100,275,25)]
    row_counter = [i-7 for i in range(7,7+ len(rows))]
    loan_below_limits = [num for num in range(int(loan_break_point.loan_break_point),min_loan - min_loan,-min_loan)]
    
    

    gci = (comp_plan.Percentage * 100) * loan_break_point.loan_break_point / 10000 + comp_plan.Flat_Fee
    if gci > comp_plan.MAX_GCI:
        gci = comp_plan.MAX_GCI
    FLAT_AM0UNT = gci - (gci/1000) * ((loan_below_limits[len(loan_below_limits) - 1] or 0) * 0.1/10000) 
    
     #F7 * J9 -> E21 * D23 /10000 + comp_flat_fee * J9(constant loan/peryear)
    annual_ahf_cap =  calculate_annual_ahf_income(loan_break_point,comp_plan,1 - float(branch.commission))
    gross_ahf_income = calculate_gross_ahf_income(loan_break_point,comp_plan,float(branch.commission))
    gross_income = calculate_gross_ahf_income(loan_break_point,comp_plan,1 - float(branch.commission))
    branch_gross = branch_gross_income(loan_break_point,comp_plan,float(branch.commission))
    flat_fee_gci = int((comp_plan.Percentage * 100) * loan_break_point.loan_break_point / 10000) 
    above_loan_break_point_ahf_commission = int(flat_fee_gci * (branch.commission))
    # social_security = calculate_social_security()
    #  calculate_social_security(loan_break_amount,comp_plan,commission,above_loan_break_point_ahf_commission,percentage,small_percentage):
    social_security = calculate_social_security(loan_break_point,comp_plan,float(1 - branch.commission),above_loan_break_point_ahf_commission,0.923199268694749
,0.062) 
    CA_Unemployment = calculate_CA_Unemployment(branch_gross)
  
    
    E23 = (bps.bps * loan_break_point.loan_break_point )/ 10000 + comp_plan.Flat_Fee 
    nums_loans = [math.ceil(get_gci_result(comp_plan, num) * float((1-branch.commission))) for num in loan_below_limits]
    annual_ahf_to_gci_result = [int(annual_ahf_cap)// num for num in  nums_loans]
    
    revenue_share = round((branch.loan_per_year / ahf.loan_per_year) * 100,2) if (branch.loan_per_year / ahf.loan_per_year) < 1 else 100
    
    
        
    bpl   = BranchPayrollLiabilities.objects.all()
    bplq  =  BranchPayrollLiabilitiesQ.objects.all()
    bplr  =  BranchPayrollLiabilitieR.objects.all().first()
    bpl_meta = BranchPayrollLiabilities._meta
    bpl_columns = [field.name for field in BranchPayrollLiabilities._meta.get_fields()]
    bpl_columns_index= [30 + index for index in range(1,len(bpl_columns))]
    column_and_index_dict = {} 
    column_and_bplqs_dict = {}
    bplqr_dict = {}
    
    print(" bplqr_dict ",bplqr_dict)
    
    for column,index in zip(bpl_columns,bpl_columns_index):
        column_and_index_dict[column] = index
        
        
    for column,q_value in zip(bpl_columns,bplq):
        column_and_bplqs_dict[column] = q_value
        
    bpl_columns.remove('branchpayrollliabilitiesq')
 
    for column in bpl_columns:
        bplqr_dict[column] = getattr(bplr,column)
        
    print(bplqr_dict ," bpqlr dict")
        
        
  

    
    
    
    bpl_columns.remove('id')
    bpl = bpl.values().first()
    
    categories = Category.objects.all()
    total_expense = calculate_total_expense()
    ewh = EmployeeWithholding.objects.all()
    ewh_meta = EmployeeWithholding._meta
    ewh_columns = [field.name for field in ewh_meta.get_fields()]
    ewh_columns.remove('id')
    ewh = ewh.values().first()
    
 
    
    
    
    ahf_annual_cap_data = {
        'annual_ahf_cap':math.ceil(annual_ahf_cap),
        'gross_ahf_income':math.ceil(gross_ahf_income),
        'gross_income': math.ceil(gross_income),
        'branch_gross_income':math.ceil(branch_gross),
        'annual_ahf_to_gci_result':annual_ahf_to_gci_result,
        
        
    }

    
    w2_branch_yearly_gross_income_data = {
        'social_security':social_security,
        'calculate_fed_un_employ':calculate_fed_un_employ(branch_gross),
        'calculate_CA_Unemployment':CA_Unemployment,
        'column_and_bplqs_dict':column_and_bplqs_dict,
        'bplqr_dict':bplqr_dict, 
      
    }

    
  
    context = {

        'categories':categories,
        'total_expense':total_expense,
        'min_compesate':comp_plan.Maximum_Compensation / 1000,
        'flat_fee_gci': flat_fee_gci, #+  comp_plan.Flat_Fee
        'above_loan_break_point_ahf_commission':above_loan_break_point_ahf_commission,
        'column_and_index_dict':column_and_index_dict,
        'bplqr':bplqr_dict,
        'bplqr_total': sum(bplqr_dict.values()),
        
        
        'ewh':dict(ewh),
        'ewh_columns':ewh_columns,
        
        'bpl':dict(bpl),
        'bpl_columns':bpl_columns,
        'w2_branch_yearly_gross_income_data':w2_branch_yearly_gross_income_data,
        
        
        'E23':E23,
        'revenue_share':revenue_share,
        'W2_branch_column_names':W2_branch_column_names,
        'comp_plan_for_lower_limit_MAX_GCI':int(comp_plan.MAX_GCI),
        'ahf_loan_per_year':ahf.loan_per_year,
        'ahf_loan_per_month':ahf.loan_per_year / 12,
        'ahf_bps':int(bps.bps) *float(1- branch.commission),
        'branch_bps':int(bps.bps) *float(branch.commission),
        'loan_below_limits':loan_below_limits,
        'loan_per_year':int(branch.loan_per_year),
        'comp_plan_for_lower_limit':comp_plan,
        'ahf_amount': math.ceil(ahf_amount) if ahf_amount > 0 else None,
        'rows':rows,
        'rows_counter':row_counter,
        'branch_amount': math.ceil(branch.commission * 100) if branch.commission > 0 else None,
        'bps':int(bps.bps) if bps.bps > 0 else None,
        'loan_break_point': math.ceil(loan_break_point.loan_break_point) ,# if loan_break_point >0 else None,
        'comp_plan':comp_plan.Flat_Fee if comp_plan.Flat_Fee > 0 else None,
        'gci': math.ceil(gci),
        'ahf_commission': math.ceil(ahf_commission) if ahf_commission > 0 else None,
        'ahf_commission_amount':  1 - float(branch.commission) if branch.commission > 0 else None ,#ahf_amount, # ahf.commission,
        'branch_commission': math.ceil(branch_commission) if branch_commission > 0 else None,
        'branch_commission_amount':branch.commission if branch.commission > 0 else None,
        'ahf_annual_cap_data':ahf_annual_cap_data,

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

def change_branch_loan(request):
    if request.method == "POST":
        # print(request.POST.get('M9'),"m9")
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
    




    
#S1 = M9 Number of loans
#P1 = M7 Branch Yearly Gross Revenue
#P19  =P1-Q16 Net income before payroll
#P17 =SUM(P8:P16) Total expenses
#P21 =P19*S21   Taxable gross payroll
# O23 = label(social security  Employee) = P23
# 030 = label(socail security Branch)  = P30
# S21 = 96.205%  iterate to get this value so that balance is less than 0.001
# R39 = P39 - Q39 
# while R39 is greater than 0.001 iterate S21 
        # if R39 is negative then S21 = S21 - increment
        # else S21 = S21 + increment
        # adjust increment
        #S1 = 96.205324% final solution balance equals 0.00
        #S1 = 96.0 balance equals -11.02 minus sign tells you 96.0 is too big 
        # S1 = 95.0 the balance equal to +3858.06 plus sign tells you 95.0 is too small 
            # increment = 0.5  initial guess halfway between 
        # S1 = 95.0 + increment 
        # S1 = 95.5 the balance equal to +1923.25 plus sign tells you 95.5 is too small
            # increment = 0.1
        # S1 = 95.5 + increment
        # S1 = 95.6 the balance equal to +1536.61 plus sign tells you 95.6 is too small
        # S1 = 95.7 the balance equal to +1149.71 plus sign tells you 95.7 is too small
        # S1 = 95.8 the balance equal to +762.80 plus sign tells you 95.8 is too small
        # S1 = 95.9 the balance equal to +375.89 plus sign tells you 95.9 is too small
        # S1 = 96.0 the balance equal to -11.02 minus sign tells you 96.0 is too big
            # increment = increment / 10
            # increment = 0.01 
        # S1 = 96.0 + increment(-0.01)
        # S1 = 95.99 the balance equal to +27.67 plus sign tells you 95.99 is too small 
            # increment equals 0.001 increment = increment / 10
        # S1 = 95.999 the balance equal to -7.15  negative sing tells you 95.999 is too big
        # S1 = 95.998 the the balance equal to -3.28 negative sign tells you 95.998 is too big
        # S2 = 95.997 the the balance equal to +0.59  plus sign tells you 95.997 is to small
        # S2 = 95.9979 the balance equal to -2.89 negative sign tells you 95.9979  is to big
        # S2 = 95.9978 the balance equal to -2.50 negative sing tells you 95.9978 is to big
        # S2 = 95.9977 the  balance equal to -2.12 negative sing tells you 95.9977 is to big
        




