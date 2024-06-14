from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.recruiter.models import Bps,LoanBreakPoint,CompPlan,AHF,Branch,Node
import math
import logging
from colorlog import ColoredFormatter
from  django.shortcuts import redirect
from utils.q22 import automate_q22_value
from django.conf import  settings
from apps.recruiter.views import bfs_traversal


context = {}

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
                    calculate_balance,
                    calculate_branch_gross_ahf_income,
                    calculate_gross_branch_income,
                    calculate_gross__new_branch_income,
                    calculate_above_loan_break_point_ahf_commission,
                    calculate_social_medicare_disability,
                    calculate_ahf_annual_cap_ahf              

    )

from utils.w2_branch import W2_branch_column_names
from utils.ahf_annual_cap_data import ahf_annual_cap_data as aacd
from apps.RevenueShare.views import total_all_revenue_share

from apps.W2branchYearlyGross.models import (
                                        Category,
                                        EmployeeWithholding,
                                        EmployeeWithholdingQ,
                                        BranchPayrollLiabilities,
                                        BranchPayrollLiabilitieQ,
                                        BranchPayrollLiabilitieR,
                                        Q22
                                
                                        )


from apps.RevenueShare.models import RevenueShare

from utils.bisect_balance import find_root,function





def home(request):
    """
        entry point of the system
    """


    # Set up the logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create a custom log formatter with colors
    formatter = ColoredFormatter(
        "%(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s",
        datefmt=None,
        reset=True,
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        },
        secondary_log_colors={},
        style='%'
    )
    
    # Create a console handler and set the formatter
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Add the console handler to the logger
    logger.addHandler(console_handler)

   

    
    
    
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
    
    try:
        bpl             = BranchPayrollLiabilities.objects.all()
    except BranchPayrollLiabilities.DoesNotExist as e:
        raise e
    
    try:
        bplq            = BranchPayrollLiabilitieQ.objects.all().first()
    except BranchPayrollLiabilitieQ.DoesNotExist as e:
        raise e
    try: 
        ewl              = EmployeeWithholding.objects.all().first()
    except EmployeeWithholding.DoesNotExist as e:
        raise e  
    try:   
        ewlq            = EmployeeWithholdingQ.objects.all().first()
    except EmployeeWithholdingQ.DoesNotExist as e:
        raise e
    try: 
        bplr           = BranchPayrollLiabilitieR.objects.all().first()
    except BranchPayrollLiabilitieR.DoesNotExist as e:
        raise e
    
    gci                =     (comp_plan.Percentage * 100) * loan_break_point.loan_break_point/10000  + comp_plan.Flat_Fee
    branch_commission  =     gci * float(branch.commission)
    ahf_commission     =     gci * (1 - float(branch.commission))
    ahf_amount         =     100 - branch.commission * 100
    
 
    
    
    MIN_LOAN = 100000 
    rows = [50] +  [num for num in range(100,275,25)]
    row_counter = [i-7 for i in range(7,7+ len(rows))]
    
    loan_below_limits = [num for num in range(int(loan_break_point.loan_break_point),MIN_LOAN - MIN_LOAN,-MIN_LOAN)]
    

    

    gci = bps.bps * loan_break_point.loan_break_point / 10000 + comp_plan.Flat_Fee
    GCI = gci
   
        
    FLAT_AM0UNT = gci - (gci/1000) * ((loan_below_limits[len(loan_below_limits) - 1] or 0) * 0.1/10000) 

    visited,node_list =  bfs_traversal(request)
    print(f"{request.user} sponsor mlo with level =",node_list)
   
  
    annual_ahf_cap              = calculate_annual_ahf_income(loan_break_point,comp_plan,1 - float(branch.commission))
    gross_ahf_income            = calculate_gross_ahf_income(loan_break_point,comp_plan,float(branch.commission))
    gross_income                = calculate_ahf_annual_cap_ahf(loan_break_point,comp_plan,1 - float(branch.commission)) 
    branch_gross                = calculate_gross_branch_income(loan_break_point,comp_plan,float(branch.commission))
    _branch_gross_income        = calculate_branch_gross_ahf_income(loan_break_point,comp_plan,1 - float(branch.commission))
    
    _branch_new_gross_income    = calculate_gross__new_branch_income(loan_break_point,comp_plan,gci,branch)

    flat_fee_gci                          = int((comp_plan.Percentage * 100) * loan_break_point.loan_break_point / 10000) 
    above_loan_break_point_ahf_commission = calculate_above_loan_break_point_ahf_commission(loan_break_point,comp_plan,branch)
    E23                                   = (bps.bps * loan_break_point.loan_break_point )/ 10000 + comp_plan.Flat_Fee 
    nums_loans                            = [get_gci_result(comp_plan, num) * float((1-branch.commission)) for num in loan_below_limits]
      
    
    annual_ahf_to_gci_result   = [gross_income/ num for num in  nums_loans]

    revenue_share               = round((branch.loan_per_year / ahf.loan_per_year) * 100,2) if (branch.loan_per_year / ahf.loan_per_year) < 1 else 100
    
    
    
        

    q22              = Q22.objects.filter(id=1).first()
    left             = Q22.objects.filter(value = 0).first()
    right            = Q22.objects.filter(value = 100).first()
    tolerance        = 1e-6
    balance,root     = find_root(function,left,right,tolerance)
    q22.value        = root
    left.save()
    right.save()
    q22.save()
    

    
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
    total_expense = calculate_total_expense(_branch_new_gross_income,above_loan_break_point_ahf_commission)
    ewh = EmployeeWithholding.objects.all()
  
    ewh_meta = EmployeeWithholding._meta
    ewh_columns = [field.name for field in ewh_meta.get_fields()]
    ewh_columns.remove('id')
    ewh = ewh.values().first()
    
 
    ahf_annual_cap_data = aacd
    
  
  
   
    
    # Employee withholding data
    _calculate_social_security              = calculate_social_security(_branch_new_gross_income,total_expense,q22) 
    CA_Unemployment                         = calculate_CA_Unemployment(branch_gross,total_expense,q22)
    medicare                                = calculate_medicare(_branch_new_gross_income,total_expense,q22)
    bplr_total                              = calculate_social_medicare_disability(_branch_new_gross_income,total_expense,q22)
    

    
    employee_with_holdings_q_columns_total  = sum(ewl_dict.values())
    total_employee_with_holding_expense     = calculate_total_employee_with_holding_expense(branch_gross,total_expense,q22)
  
    CA_Unemployment_payroll_liabilities = calculate_CA_Unemployment_payroll_liabilities(branch_gross,total_expense,q22)
    medicare_payroll_liabilities                                = calculate_medicare_payroll_liabilities(branch_gross,total_expense,q22)
    _calculate_CA_Disability            = calculate_CA_Disability(_branch_new_gross_income,total_expense,q22) 
    calcuate_Fed_Unemploy               = calculate_fed_un_employ_payroll_liabilities(branch_gross,total_expense,q22)
    _calculate_ett                      = calculate_ett(branch_gross,total_expense,q22)
    branch_payroll_liabilities_total    = calculate_branch_payroll_liabilities_total(_branch_new_gross_income,total_expense,q22)
    
    
    debit                               = calculate_debit(_branch_new_gross_income,total_expense,q22) 
    
    
    
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
        'net_income_before_payroll'     :_branch_new_gross_income - total_expense,
        'w2_Taxable_gross_payroll'      :(_branch_new_gross_income - total_expense) * q22.value/100,
        'q22'                           :q22.value,
      
    }
    

    
      
    w2_branch_payroll_liabilities_data = {
        'calculate_fed_un_employ_payroll_liabilities '       :calculate_fed_un_employ_payroll_liabilities(branch_gross,total_expense,q22),
        'CA_Unemployment_payroll_liabilities'                :CA_Unemployment_payroll_liabilities,
        'calculate_Medicare_payroll_liabilities '            :medicare_payroll_liabilities,
       
      
      
    }
    
    revenues   =  {
        "all_revenues":RevenueShare.objects.all(),
        'first_revenues':RevenueShare.objects.all()[1],
        "total_all_revenue_share":total_all_revenue_share
    }
    
    
    bps_from_50_to_250 = []
    branch_for_bps_from_50_to_250 = []
    gci_for_bps_from_50_to_250 = []
    ahf_for_bps_from_50_to_250 = []
    
    if comp_plan.Percentage == 0.0:
        bps_from_50_to_250            = [0,0] + [num*comp_plan.Percentage for num in range(100,250,25)]+[0]
    else:
        bps_from_50_to_250            = [50,100] + [num for num in range(100,250,25)]+[250]

        
    
    
    if comp_plan.Percentage != 0.0:
        gci_for_bps_from_50_to_250    = [gci/(num) * 10000 for num in bps_from_50_to_250] 
    
        ahf_for_bps_from_50_to_250    = [(1 - branch.commission) * num for num in bps_from_50_to_250] 
        branch_for_bps_from_50_to_250 = [branch.commission* num for num in bps_from_50_to_250]

    bps_to_gci_dict               = {}
    bps_to_ahf_commission_dict    = {}
    bps_to_branch_commission_dict = {}
    


    
    for key,value in zip(bps_from_50_to_250,gci_for_bps_from_50_to_250):
        bps_to_gci_dict[key] = value
        
    for key,value in zip(bps_from_50_to_250,ahf_for_bps_from_50_to_250):
        bps_to_ahf_commission_dict[key] = value
        
    for key,value in zip(bps_from_50_to_250,branch_for_bps_from_50_to_250):
     
            
        bps_to_branch_commission_dict[key] = value
    
    credit = _branch_new_gross_income
    tolerance    = 1e-6
    balance = credit - debit
  
    
        
    
        
         
    context = {
        'bps_from_50_to_250':bps_from_50_to_250,
        'bps_to_gci_dict':bps_to_gci_dict,
        'bps_to_ahf_commission_dict':bps_to_ahf_commission_dict,
        'bps_to_branch_commission_dict':bps_to_branch_commission_dict,
        'categories':categories,
        'total_expense':total_expense,
        'min_compesate':comp_plan.Maximum_Compensation / 1000,
        'flat_fee_gci': flat_fee_gci, #+  comp_plan.Flat_Fee
        'above_loan_break_point_ahf_commission':above_loan_break_point_ahf_commission,
        'column_and_index_dict':column_and_index_dict,
        'bplqr'     :bplqr_dict,
        'bplq_dict' :bplq_dict,
        'ewl_dict'  :ewl_dict,
        'bplr_total':sum(bplqr_dict.values()),
        'bplq_total':sum(bplq_dict.values()),
        'bplr_total':bplr_total,
        'debit'     :debit,
        'MIN_LOAN'  :MIN_LOAN,
        'balance'   :balance ,# _branch_new_gross_income - debit ,#       balance,
        
        'employee_with_holdings_q_columns_total':employee_with_holdings_q_columns_total,
        'net_paycheck_for_employee_with_holdings_total':net_paycheck_for_employee_with_holdings(
            _branch_new_gross_income,
            # branch_gross,
            total_expense,
            q22,
            bplr_total
            ),
        
        "calculate_ett_num":_calculate_ett,
        "branch_payroll_liabilities_percentate_total":branch_payroll_liabilities_percentate_total,
        "branch_payroll_liabilities_total"  :branch_payroll_liabilities_total,
        
        'ewh'                               :dict(ewh),
        'ewh_columns'                       :ewh_columns,
        
        'bpl'                               :dict(bpl),
        'bpl_columns'                       :bpl_columns,
        'w2_branch_yearly_gross_income_data':w2_branch_yearly_gross_income_data,
        'w2_branch_payroll_liabilities_data':w2_branch_payroll_liabilities_data,
        
        
        'E23'                              :E23,
        'revenue_share'                    :revenue_share,
        'W2_branch_column_names'           :W2_branch_column_names,
        'comp_plan_for_lower_limit_MAX_GCI':int(comp_plan.MAX_GCI),
        'ahf_loan_per_year'                :ahf.loan_per_year,
        'ahf_loan_per_month'               :ahf.loan_per_year / 12,
        'ahf_bps'                          :bps.bps *float(1- branch.commission),
        'branch_bps'                       :bps.bps *float(branch.commission),
        'loan_below_limits'                :loan_below_limits,
        'loan_per_year'                    :branch.loan_per_year,
        'comp_plan_for_lower_limit'        :comp_plan,
        'ahf_amount'                       :ahf_amount if ahf_amount > 0 else None,
        'rows'                             :rows,
        'rows_counter'                     :row_counter,
        'branch_amount'                    :branch.commission * 100 if branch.commission > 0 else None,
        'bps'                              :bps.bps if bps.bps > 0 else None,
        'loan_break_point'                 :loan_break_point.loan_break_point ,# if loan_break_point >0 else None,
        'comp_plan'                        :comp_plan.Flat_Fee if comp_plan.Flat_Fee > 0 else None,
        'GCI'                              :GCI,
        'ahf_commission'                   :ahf_commission if ahf_commission > 0 else None,
        'ahf_commission_amount'            :1 - float(branch.commission) if branch.commission > 0 else None ,#ahf_amount, # ahf.commission,
        'branch_commission'                :branch_commission if branch_commission > 0 else None,
        'branch_commission_amount'         :branch.commission if branch.commission > 0 else None,
        'ahf_annual_cap_data'              :ahf_annual_cap_data,
        'revenues'                         :revenues,
        'version'                          :settings.VERSION

    }
    return render(request,"home/entry.html",context)



