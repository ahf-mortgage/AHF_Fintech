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

from apps.recruiter.models import Bps,LoanBreakPoint,CompPlan,AHF,Branch


def ahf_annual_cap_data(request):
    try:
        bps              = Bps.objects.filter(user = request.user).first()
    except Bps.DoesNotExist as e:
        raise e
            
    try:
        loan_break_point = LoanBreakPoint.objects.filter(user = request.user).first()
    except LoanBreakPoint.DoesNotExist as e:
        raise e
        
    try:
        comp_plan        = CompPlan.objects.filter(user = request.user).first()
    except CompPlan.DoesNotExist as e:
        raise e
        
    try:
        ahf              = AHF.objects.all().first() 
    except AHF.DoesNotExist as e:
        raise e
    try:
            
        branch           = Branch.objects.filter(user = request.user).first() 
    except Branch.DoesNotExist as e:
        raise e
        
    
    gci               = (comp_plan.Percentage * 100) * loan_break_point.loan_break_point/10000  + comp_plan.Flat_Fee
    branch_commission = gci * float(branch.commission)
    ahf_commission    = gci * (1 - float(branch.commission))
    ahf_amount        = 100 - branch.commission * 100
    MIN_LOAN          = 100000 
    loan_below_limits = [num for num in range(int(loan_break_point.loan_break_point),MIN_LOAN - MIN_LOAN,-MIN_LOAN)]
    nums_loans        = [get_gci_result(comp_plan, num) * float((1-branch.commission)) for num in loan_below_limits]


    annual_ahf_cap            = calculate_annual_ahf_income(loan_break_point,comp_plan,1 - float(branch.commission))
    gross_ahf_income          = calculate_gross_ahf_income(request,loan_break_point,comp_plan,float(branch.commission))
    gross_income              = calculate_ahf_annual_cap_ahf(request,loan_break_point,comp_plan,1 - float(branch.commission)) 
    _branch_gross_income      = calculate_branch_gross_ahf_income(request,loan_break_point,comp_plan,1 - float(branch.commission))
    _branch_new_gross_income  = calculate_gross__new_branch_income(loan_break_point,comp_plan,gci,branch)
    annual_ahf_to_gci_result  = [gross_income/ num if num != 0 else 1 for num in  nums_loans]
    return   {
            'annual_ahf_cap'          :annual_ahf_cap,
            'gross_ahf_income'        :gross_ahf_income,
            'gross_income'            :gross_income,
            'branch_income'           :branch_gross_income,
            'branch_gross_income'     :_branch_new_gross_income,
            'annual_ahf_to_gci_result':annual_ahf_to_gci_result,
            'test_branch_gross_income':_branch_gross_income,
            'test2_branch_gross_income':_branch_new_gross_income,
            'ahf_amount'               :ahf_amount


        }
    

