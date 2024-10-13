import bisect
from utils.calc_res import calculate_balance,calculate_gross__new_branch_income,calculate_total_expense,calculate_above_loan_break_point_ahf_commission,calculate_debit
from apps.recruiter.models import LoanBreakPoint,CompPlan,Branch
from apps.W2branchYearlyGross.models import Q22
from utils.formatter import logger


def init_data(request):

    loan_break_point                      = LoanBreakPoint.objects.filter(user = request.user).first()
    comp_plan                             = CompPlan.objects.filter(user= request.user).first()
    branch                                = Branch.objects.filter(user = request.user).first()  
    gci                                   = (comp_plan.Percentage * 100) * loan_break_point.loan_break_point/10000  + comp_plan.Flat_Fee
    branch_gross                          = calculate_gross__new_branch_income(request,loan_break_point,comp_plan,gci)
    above_loan_break_point_ahf_commission = calculate_above_loan_break_point_ahf_commission(loan_break_point,comp_plan,branch) #int(flat_fee_gci * (branch.commission))
    total_expense                         = calculate_total_expense(branch_gross,above_loan_break_point_ahf_commission)

    # print("comp plance percentage",comp_plan.Percentage)
    # print("Minimum_Compensation=",comp_plan.Minimum_Compensation)
    # print("Maximum_Compensation=",comp_plan.Maximum_Compensation)
    # print("MAX_GCI=",comp_plan.MAX_GCI)
    # print("FF_MIN_LOAN=",comp_plan.FF_MIN_LOAN)
    # print("Flat fee=",comp_plan.Flat_Fee)

    return loan_break_point,comp_plan,gci,branch,branch_gross,above_loan_break_point_ahf_commission,total_expense



def function(request,q22):
        loan_break_point = init_data(request)[0]
        comp_plan  = init_data(request)[1]   
        gci =  init_data(request)[2]
        branch = init_data(request)[3]
        branch_gross = init_data(request)[4]
        above_loan_break_point_ahf_commission = init_data(request)[5]
        total_expense  = init_data(request)[5]
        branch_gross                          = calculate_gross__new_branch_income(request,loan_break_point,comp_plan,gci)
        above_loan_break_point_ahf_commission = calculate_above_loan_break_point_ahf_commission(loan_break_point,comp_plan,branch) #int(flat_fee_gci * (branch.commission))
        total_expense                         = calculate_total_expense(branch_gross,above_loan_break_point_ahf_commission)
        
        print("loan_break_point=,",loan_break_point)
        print("comp_plan=,",comp_plan)
        print("gci=,",gci)
        print("branch=",branch)
      
        print("above_loan_break_point_ahf_commission=,",above_loan_break_point_ahf_commission)
        print("total_expense=,",total_expense)
      
        return calculate_balance(request,branch_gross,total_expense,q22)


credit = None


def find_root(request,function, left, right, tolerance):
        debit     = None
        loan_break_point = init_data(request)[0]

    
        comp_plan  = init_data(request)[1]   
        gci = init_data(request)[2]
        branch = init_data(request)[3]
        branch_gross = init_data(request)[4]
        above_loan_break_point_ahf_commission = init_data(request)[5]
        total_expense  = init_data(request)[5]
        credit = calculate_gross__new_branch_income(request,loan_break_point,comp_plan,gci)


        if function(request,left) * function(request,right) >= 0:
            raise ValueError("Root not found in the given interval.")
        
        _left = left.value if left != None else 0
        _right = right.value
        midpoint = None
        while abs(_right - _left) > tolerance:
        
            _left = left.value if left != None else 0
            _right = right.value
            _midpoint = (_left + _right) / 2
            midpoint  = Q22(value = _midpoint)
            right     = Q22(value = _right)
            left      = Q22(value = _left)
            debit = calculate_debit(request,branch_gross,total_expense,Q22(value = _left + _right /2))

            
            if function(request,midpoint) == 0 :
                return midpoint
            elif function(request,midpoint) * function(request,left) < 0:
                right = midpoint               
            else:
                left = midpoint
        balance = function(request,midpoint)
        return balance,( _left + _right )/ 2
    

