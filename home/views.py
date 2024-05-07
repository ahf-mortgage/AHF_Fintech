from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from recruiter.models import Bps,LoanBreakPoint,CompPlan,AHF,Branch
import math
import logging
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
                    calculate_ett,
                    calculate_fed_un_employ,
                    calculate_CA_Unemployment,
                    calculate_CA_Disability,
                    net_paycheck_for_employee_with_holdings,
                    calculate_social_security_payroll_liabilities,
                    calculate_medicare_payroll_liabilities,
                    calculate_fed_un_employ_payroll_liabilities,
                    calculate_CA_Unemployment_payroll_liabilities,
                    calculate_branch_payroll_liabilities_total,
                    calculate_total_employee_with_holding_expense,
                    calculate_debit,
                    calculate_balance

    )

from utils.w2_branch import W2_branch_column_names
from W2branchYearlyGross.models import (
                                        Category,
                                        EmployeeWithholding,
                                        EmployeeWithholdingQ,
                                        BranchPayrollLiabilities,
                                        BranchPayrollLiabilitieQ,
                                        BranchPayrollLiabilitieR,
                                        Q22
                                
                                        )





def home(request):
    """
        This function display comp plan,loan above limit and loan below limit
    """
    try:
        bps              = Bps.objects.all().first()
    except Bps.DoesNotExist as e:
        raise e
        
    try:
        loan_break_point = LoanBreakPoint.objects.all().first()
    except LoanBreakPoint.DoesNotExist as e:
        raise e
    
    try:
        comp_plan        = CompPlan.objects.all().first()
    except CompPlan.DoesNotExist as e:
        raise e
    
    try:
        ahf              = AHF.objects.all().first() 
    except AHF.DoesNotExist as e:
        raise e
    try:
        
        branch           = Branch.objects.all().first() 
    except Branch.DoesNotExist as e:
        raise e
    
    
    logging.basicConfig(level=logging.DEBUG)  
    logger = logging.getLogger(__name__)

    
    
    bpl                     = BranchPayrollLiabilities.objects.all()
    bplq                    = BranchPayrollLiabilitieQ.objects.all().first()
    ewl                     = EmployeeWithholding.objects.all().first()
    ewlq                    = EmployeeWithholdingQ.objects.all().first()
    bplr                    = BranchPayrollLiabilitieR.objects.all().first()
    
    gci                    = (comp_plan.Percentage * 100) * loan_break_point.loan_break_point/10000  #+ comp_plan.Flat_Fee
    branch_commission   = gci * float(branch.commission)
    ahf_commission      = gci * (1 - float(branch.commission))
    ahf_amount          = 100 - branch.commission * 100
    
    
    
    MIN_LOAN = 100000 
    rows = [50] +  [num for num in range(100,275,25)]
    row_counter = [i-7 for i in range(7,7+ len(rows))]
    loan_below_limits = [num for num in range(int(loan_break_point.loan_break_point),MIN_LOAN - MIN_LOAN,-MIN_LOAN)]
    
    

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
  
    

    
    E23 = (bps.bps * loan_break_point.loan_break_point )/ 10000 + comp_plan.Flat_Fee 
    nums_loans = [math.ceil(get_gci_result(comp_plan, num) * float((1-branch.commission))) for num in loan_below_limits]
    annual_ahf_to_gci_result = [int(gross_income)// num for num in  nums_loans]
       
  
    revenue_share = round((branch.loan_per_year / ahf.loan_per_year) * 100,2) if (branch.loan_per_year / ahf.loan_per_year) < 1 else 100
    
    
    
        

    q22                     = Q22.objects.all().first()
    bpl_meta                = BranchPayrollLiabilities._meta
    bpl_columns             = [field.name for field in BranchPayrollLiabilities._meta.get_fields()]
    ewl_columns             = [field.name for field in EmployeeWithholding._meta.get_fields()]
    bplq_columns            = [field.name for field in BranchPayrollLiabilitieQ._meta.get_fields()]
    bpl_columns_index       = [30 + index for index in range(1,len(bpl_columns))]
    column_and_index_dict   = {} 
    column_and_bplqs_dict   = {}
    bplqr_dict              = {}
    bplq_dict               = {}
    ewl_dict                = {}
    bplq_dict               = {}
    
    
    
    for column,index in zip(bpl_columns,bpl_columns_index):
        column_and_index_dict[column] = index
        
    for column in bpl_columns:
        bplqr_dict[column] = getattr(bplr,column)
        
    for column in bpl_columns:
        bplq_dict[column] = getattr(bplq,column)
        
        
    for column in ewl_columns:
        ewl_dict[column] = getattr(ewlq,column)
        
 
        
        
    bpl_columns.remove('id')
    bpl = bpl.values().first()
    categories = Category.objects.all()
    total_expense = calculate_total_expense(branch_gross,gross_ahf_income)
    ewh = EmployeeWithholding.objects.all()
  
    ewh_meta = EmployeeWithholding._meta
    ewh_columns = [field.name for field in ewh_meta.get_fields()]
    ewh_columns.remove('id')
    ewh = ewh.values().first()
    
 
    
    
    
    ahf_annual_cap_data = {
        'annual_ahf_cap'            :annual_ahf_cap,
        'gross_ahf_income'          :gross_ahf_income,
        'gross_income'              :gross_income,
        'branch_gross_income'       :branch_gross,
        'annual_ahf_to_gci_result'  :annual_ahf_to_gci_result,
        
        
    }
  
   
    # q22 range(1-90) increment 1 
    # q22 range(90 - 100) increment x
    q22.value = 95
    balance = calculate_balance(branch_gross,total_expense,q22)
   
    increment = 1
    j = 0
  
    # while abs(balance) > 0.001 and j < 60:
    #     print("j= ",j)
    #     print("========================================")

    #     print("q22a= ",q22.value)
    #     print("balance= ",balance)
    #     print("incrementa= ",increment)
    #     i = 0
    #     print("i= ",i)

    #     print("incrementb= ",increment)
    #     print("q22b= ",q22.value)
    #     print("balance ",balance)

    #     print("+++++++++++++++++++++++++++++++++++++++++++")
    #     # balance is too low, need to raise to q22
    #     while balance > 0 and i < 10:
    #         q22.value = q22.value + increment
    #         # increment = 
    #         # print("increment= ",increment)
    #         balance = calculate_balance(branch_gross,total_expense,q22)

    #         print("incrementc= ",increment)
    #         print("q22c= ",q22.value)
    #         print("balance ",balance)

    #         i = i + 1
            
    #     # balance is still too low, need to raise to q22
    #     k = 0
    #     while balance > 0 and k < 10:
    #         increment = increment /10
    #         print("incrementK= ",increment)
    #         q22.value = q22.value + increment
    #         balance = calculate_balance(branch_gross,total_expense,q22)
    #         print("incrementK= ",increment)
    #         print("q22c= ",q22.value)
    #         print("balance ",balance)
    #         k = k + 1
    #         # balance is too low we need to increase q22 
    #         print("++++++++++++++++++++++++++++++++++++++++++++++")
            
            
    #     # balance is too high,need to lower q22
    #     i = 0
    #     while balance < 0 and i < 160:
    #         q22.value = q22.value - increment + increment/2
    #         increment = increment / 10
    #         print("incrementd= ",increment)
    #         balance = calculate_balance(branch_gross,total_expense,q22)
    #         print("q22 ",q22.value)
    #         print("balance ",balance)
    #         i = i + 1
        
        
    #     # balance is still too high , need to lower q22 by current increment
    #     p = 0 
    #     while balance < 0 and p < 160:
    #         q22.value = q22.value - increment
    #         balance = calculate_balance(branch_gross,total_expense,q22)

    #         print("incremente= ",increment)
    #         print("q22d= ",q22.value)
    #         print("balance ",balance)

    #         p = p + 1
    #     j = j + 1
      



        
    while abs(balance) > 0.001 and j < 10:
        print("j= ",j)
        print("========================================")

        print("q22a= ",q22.value)
        print("balance= ",balance)
        print("incrementa= ",increment)
        i = 0
        print("i= ",i)

        print("incrementb= ",increment)
        print("q22b= ",q22.value)
        print("balance ",balance)

        print("+++++++++++++++++++++++++++++++++++++++++++")
        # balance is too low, need to raise to q22
        while balance > 0 and i < 160:
            q22.value = q22.value + increment
            # increment = 
            # print("increment= ",increment)
            balance = calculate_balance(branch_gross,total_expense,q22)

            print("incrementc= ",increment)
            print("q22c= ",q22.value)
            print("balance ",balance)
            k = 0
            # balance is still too low need to raise q22
            while balance > 0 and k < 80:
                q22.value = q22.value + increment
                print("q22K= ",q22.value)
                balance = calculate_balance(branch_gross,total_expense,q22)
                print("balanceK= ",balance)
                
                k = k + 1

            i = i + 1
        #balance is too high,need to lower q22
        i = 0
        while balance < 0 and i < 80:
            q22.value = q22.value - increment + increment/2
            increment = increment / 10
            print("incrementd= ",increment)
            if increment < 0.0001:
                print("increment < 0.0001")
                break
            balance = calculate_balance(branch_gross,total_expense,q22)
            print("q22F ",q22.value)
            print("balance ",balance)
            
            # balance is still too high , need to lower q22 by current increment
            p = 0 
            while balance < 0 and p < 40:
                q22.value = q22.value - increment
                balance = calculate_balance(branch_gross,total_expense,q22)

                print("incremente= ",increment)
                print("q22d= ",q22.value)
                print("balance ",balance)

                p = p + 1
            i = i + 1

        j = j + 1
      

        
        

    
    # Employee withholding data
    _calculate_social_security              = calculate_social_security(branch_gross,total_expense,q22) 
    CA_Unemployment                         = calculate_CA_Unemployment(branch_gross,total_expense,q22)
    medicare                                = calculate_medicare(branch_gross,total_expense,q22)
    
    bplr_total                              = _calculate_social_security + calculate_CA_Disability(branch_gross,total_expense,q22)  + medicare
   
    
    
    employee_with_holdings_q_columns_total  = sum(ewl_dict.values())
    total_employee_with_holding_expense     = calculate_total_employee_with_holding_expense(branch_gross,total_expense,q22) #(branch_gross - total_expense)* q22.value/100
  
    
    # _payroll_liabilities
    _calculate_social_security_payroll_liabilities              = calculate_social_security_payroll_liabilities(branch_gross,total_expense,q22) 
    CA_Unemployment_payroll_liabilities                         = calculate_CA_Unemployment_payroll_liabilities(branch_gross,total_expense,q22)
    medicare_payroll_liabilities                                = calculate_medicare_payroll_liabilities(branch_gross,total_expense,q22)
    _calculate_CA_Disability                                    = calculate_CA_Disability(branch_gross,total_expense,q22) 
    calcuate_Fed_Unemploy                                       = calculate_fed_un_employ_payroll_liabilities(branch_gross,total_expense,q22)
    _calculate_ett                                              = calculate_ett(branch_gross,total_expense,q22)
    
    branch_payroll_liabilities_total                            = calculate_branch_payroll_liabilities_total(branch_gross,total_expense,q22)
    debit                                                       = calculate_debit(branch_gross,total_expense,q22) # total_expense  + total_employee_with_holding_expense + branch_payroll_liabilities_total 
    branch_payroll_liabilities_percentate_total                 = bplq.Social_Security + bplq.Medicare +bplq.CA_Unemployment + bplq.Fed_Unemploy + bplq.Employment_Training_Tax
   
   
    w2_branch_yearly_gross_income_data = {
        'calculate_social_security'     :_calculate_social_security,
        'calculate_fed_un_employ'       :calculate_fed_un_employ(branch_gross),
        'calculate_CA_Disability'       :_calculate_CA_Disability,
        'calculate_CA_Unemployment'     :CA_Unemployment,
        'calculate_fed_un_employ_payroll_liabilities'       :calculate_fed_un_employ_payroll_liabilities(branch_gross,total_expense,q22),
        'calculate_Medicare'            :medicare,
        'column_and_bplqs_dict'         :column_and_bplqs_dict,
        'bplqr_dict'                    :bplqr_dict, 
        'bplq_dict'                     :bplq_dict,
        'net_income_before_payroll'     :branch_gross - total_expense,
        'w2_Taxable_gross_payroll'      :(branch_gross - total_expense) * q22.value/100,
        'q22'                           :q22.value,
       
      
    }
    

    
      
    w2_branch_payroll_liabilities_data = {
        
        'calculate_social_security_payroll_liabilities '     :_calculate_social_security_payroll_liabilities,
        'calculate_fed_un_employ_payroll_liabilities '       :calculate_fed_un_employ_payroll_liabilities(branch_gross,total_expense,q22),
        'CA_Unemployment_payroll_liabilities'                :CA_Unemployment_payroll_liabilities,
        'calculate_Medicare_payroll_liabilities '            :medicare_payroll_liabilities,
       
      
      
    }

    # Above  loan break points data
    # range of numbers from 50 to 250 within 50 interval
    #gci =IF(B10>0,$C$8/B10*10000,0 )
    bps_from_50_to_250          = [50,100] + [num for num in range(100,250,25)]+[250]
    gci_for_bps_from_50_to_250  = [gci/(num) * 10000 for num in bps_from_50_to_250] 
    ahf_for_bps_from_50_to_250  = [(1 - branch.commission) * num for num in bps_from_50_to_250] 
    branch_for_bps_from_50_to_250 = [branch.commission* num for num in bps_from_50_to_250]
    bps_to_gci_dict             = {}
    bps_to_ahf_commission_dict  = {}
    bps_to_branch_commission_dict = {}

    
    for key,value in zip(bps_from_50_to_250,gci_for_bps_from_50_to_250):
        bps_to_gci_dict[key] = value
        
    for key,value in zip(bps_from_50_to_250,ahf_for_bps_from_50_to_250):
        bps_to_ahf_commission_dict[key] = value
        
    for key,value in zip(bps_from_50_to_250,branch_for_bps_from_50_to_250):
        bps_to_branch_commission_dict[key] = value
        
  
    context = {
        'bps_from_50_to_250':bps_from_50_to_250,
        'bps_to_gci_dict':bps_to_gci_dict,
        'bps_to_ahf_commission_dict':bps_to_ahf_commission_dict,
        'bps_to_branch_commission_dict':bps_to_branch_commission_dict,
        'categories':categories,
        'total_expense':int(total_expense),
        'min_compesate':comp_plan.Maximum_Compensation / 1000,
        'flat_fee_gci': flat_fee_gci, #+  comp_plan.Flat_Fee
        'above_loan_break_point_ahf_commission':above_loan_break_point_ahf_commission,
        'column_and_index_dict':column_and_index_dict,
        'bplqr':bplqr_dict,
        'bplq_dict':bplq_dict,
        'ewl_dict':ewl_dict,
        'bplr_total': sum(bplqr_dict.values()),
        'bplq_total': sum(bplq_dict.values()),
        'bplr_total': bplr_total,
        'debit':debit,
        'balance':branch_gross- debit,
        'employee_with_holdings_q_columns_total':employee_with_holdings_q_columns_total,
        
        
        'net_paycheck_for_employee_with_holdings_total':net_paycheck_for_employee_with_holdings(
            branch_gross,
            math.ceil(total_expense),
            q22,
            bplr_total
            ),
        
        
        
        "calculate_ett_num":_calculate_ett,
        "branch_payroll_liabilities_percentate_total":branch_payroll_liabilities_percentate_total,
        "branch_payroll_liabilities_total":branch_payroll_liabilities_total,
        
        'ewh':dict(ewh),
        'ewh_columns':ewh_columns,
        
        'bpl':dict(bpl),
        'bpl_columns':bpl_columns,
        'w2_branch_yearly_gross_income_data':w2_branch_yearly_gross_income_data,
        'w2_branch_payroll_liabilities_data':w2_branch_payroll_liabilities_data,
        
        
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
        'ahf_amount': ahf_amount if ahf_amount > 0 else None,
        'rows':rows,
        'rows_counter':row_counter,
        'branch_amount': branch.commission * 100 if branch.commission > 0 else None,
        'bps':int(bps.bps) if bps.bps > 0 else None,
        'loan_break_point': loan_break_point.loan_break_point ,# if loan_break_point >0 else None,
        'comp_plan':comp_plan.Flat_Fee if comp_plan.Flat_Fee > 0 else None,
        'gci': gci,
        'ahf_commission': ahf_commission if ahf_commission > 0 else None,
        'ahf_commission_amount':  1 - float(branch.commission) if branch.commission > 0 else None ,#ahf_amount, # ahf.commission,
        'branch_commission': branch_commission if branch_commission > 0 else None,
        'branch_commission_amount':branch.commission if branch.commission > 0 else None,
        'ahf_annual_cap_data':ahf_annual_cap_data,

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
        




