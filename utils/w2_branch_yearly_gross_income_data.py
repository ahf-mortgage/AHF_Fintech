from recruiter.models import(
                            Bps,
                            LoanBreakPoint,
                            CompPlan,
                            AHF,
                            Branch
                             )

from W2branchYearlyGross.models import (
                                        Category,
                                        EmployeeWithholding,
                                        EmployeeWithholdingQ,
                                        BranchPayrollLiabilities,
                                        BranchPayrollLiabilitieQ,
                                        BranchPayrollLiabilitieR,
                                        Q22
                                
                                        )
from .calc_res import (
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
                    calculate_social_medicare_disability                 

    )


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
        bpl                     = BranchPayrollLiabilities.objects.all()
except BranchPayrollLiabilities.DoesNotExist as e:
        raise e
    
try:
        bplq                    = BranchPayrollLiabilitieQ.objects.all().first()
except BranchPayrollLiabilitieQ.DoesNotExist as e:
        raise e
try: 
        ewl                     = EmployeeWithholding.objects.all().first()
except EmployeeWithholding.DoesNotExist as e:
        raise e  
try:   
        ewlq                    = EmployeeWithholdingQ.objects.all().first()
except EmployeeWithholdingQ.DoesNotExist as e:
        raise e
try: 
    bplr                    = BranchPayrollLiabilitieR.objects.all().first()
except BranchPayrollLiabilitieR.DoesNotExist as e:
    raise e
        
        

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
        

annual_ahf_cap                             =  calculate_annual_ahf_income(loan_break_point,comp_plan,1 - float(branch.commission))
gross_ahf_income                           = calculate_gross_ahf_income(loan_break_point,comp_plan,float(branch.commission))
gross_income                               = calculate_gross_ahf_income(loan_break_point,comp_plan,1 - float(branch.commission))


branch_gross                               = calculate_gross_branch_income(loan_break_point,comp_plan,float(branch.commission))
_branch_gross_income                       = calculate_branch_gross_ahf_income(loan_break_point,comp_plan,1 - float(branch.commission))
_branch_new_gross_income                   = calculate_gross__new_branch_income(loan_break_point,comp_plan,gci,branch)



CA_Unemployment_payroll_liabilities        = calculate_CA_Unemployment_payroll_liabilities(branch_gross,total_expense,q22)
medicare_payroll_liabilities               = calculate_medicare_payroll_liabilities(branch_gross,total_expense,q22)
_calculate_CA_Disability                   = calculate_CA_Disability(_branch_new_gross_income,total_expense,q22) 



calcuate_Fed_Unemploy                       = calculate_fed_un_employ_payroll_liabilities(branch_gross,total_expense,q22)
_calculate_ett                              = calculate_ett(branch_gross,total_expense,q22)
branch_payroll_liabilities_total            = calculate_branch_payroll_liabilities_total(_branch_new_gross_income,total_expense,q22)
debit                                       = calculate_debit(_branch_new_gross_income,total_expense,q22)

for key,value in zip(bps_from_50_to_250,gci_for_bps_from_50_to_250):
    bps_to_gci_dict[key] = value
        
for key,value in zip(bps_from_50_to_250,ahf_for_bps_from_50_to_250):
    bps_to_ahf_commission_dict[key] = value
        
for key,value in zip(bps_from_50_to_250,branch_for_bps_from_50_to_250):
    bps_to_branch_commission_dict[key] = value
        



branch_payroll_liabilities_percentate_total   = bplq.Social_Security + bplq.Medicare +bplq.CA_Unemployment + bplq.Fed_Unemploy + bplq.Employment_Training_Tax
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
    
