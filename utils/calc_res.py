import math
import logging
from colorlog import ColoredFormatter
from apps.recruiter.models import  *
from apps.W2branchYearlyGross.models import (
                     BranchPayrollLiabilitieR,
                     BranchPayrollLiabilitieQ,
                     EmployeeWithholdingR,
                     EmployeeWithholdingQ
)

from apps.W2branchYearlyGross.models import *
from utils.formatter import logger






bps = Bps.objects.all().first().bps

def calculate_above_loan_break_point_ahf_commission(loan_break_point,comp_plan,branch):
    gci = bps * loan_break_point.loan_break_point / 10000 + comp_plan.Flat_Fee
    # return  float(comp_plan.Percentage * 100) * float(loan_break_point.loan_break_point / 10000)   * float(branch.commission)
    return gci * float(branch.commission)



def calculate_annual_ahf_income(loan_break_amount,comp_plan,ahf_comission_amount):
    """
       annual income commission 
    """
    return( (275 * loan_break_amount.loan_break_point )/ 10000 + comp_plan.Flat_Fee )* ahf_comission_amount * 21



def calculate_gross_ahf_income(loan_break_amount,comp_plan,commission,value = 275):
    """
        ahf gross income commission 
        K8=IF(K10<=H10,E8*K10,H8+$C8*(K10-H$10))
    """
    ahf     = AHF.objects.all().first()   # left side table
    branch  = Branch.objects.all().first() # right side table
    K10     = branch.loan_per_year
    H10     = ahf.loan_per_year
    E8      = calculate_above_loan_break_point_ahf_commission(loan_break_amount,comp_plan,branch)
    gci     = (comp_plan.Percentage * 100) * loan_break_amount.loan_break_point/10000  + comp_plan.Flat_Fee
    D8      = gci * (1 - float(branch.commission))
    G8      = D8 * H10
    
    return E8 * H10
 
    


def calculate_ahf_annual_cap_ahf(loan_break_amount,comp_plan,commission,value = 275):
    """
        ahf gross income commission 
        K8=IF(K10<=H10,E8*K10,H8+$C8*(K10-H$10))
    """
    
  
    ahf     = AHF.objects.all().first()   # left side table
    branch  = Branch.objects.all().first() # right side table
    K10     = ahf.loan_per_year
    H10     = ahf.loan_per_year
    E8      = calculate_above_loan_break_point_ahf_commission(loan_break_amount,comp_plan,branch)
    gci     = (comp_plan.Percentage * 100) * loan_break_amount.loan_break_point/10000  + comp_plan.Flat_Fee
    D8      = gci * (1 - float(branch.commission))
    G8      = D8 * H10
    print("G8=",G8)
    print("D8=",D8)
    print("H10=",H10)
    
    return G8










def calculate_gross_branch_income(loan_break_amount,comp_plan,commission,value = 275):
    """
        ahf gross income commission 
        IF(K10<=H10,K10*D8,G8)
    """
    ahf     = AHF.objects.all().first()   # left side table
    branch  = Branch.objects.all().first() # right side table
    # if branch.loan_per_year <= ahf.loan_per_year:
    #     # branch.loan_per_year 
    
    loans_per_year = ahf.loan_per_year
    total = ((value * loan_break_amount.loan_break_point )/ 10000 + comp_plan.Flat_Fee)* commission * loans_per_year
    return  total



# branch_amount =  275 * loan_amout_break / 10000 + comp.Flat_Fee * branch.commission*  21
def calculate_branch_gross_ahf_income(loan_break_amount,comp_plan,commission,value = 275):
    """
        ahf gross income commission 
        =IF(K10<=H10,K10*D8,G8)
    """
    
    ahf     = AHF.objects.all().first()   # left side table
    branch  = Branch.objects.all().first() # right side table
    K10     = ahf.loan_per_year
    H10     = branch.loan_per_year
    E8      = calculate_above_loan_break_point_ahf_commission(loan_break_amount,comp_plan,branch)
    gci     = (comp_plan.Percentage * 100) * loan_break_amount.loan_break_point/10000  + comp_plan.Flat_Fee
    D8      = gci * (1 - float(branch.commission))
    G8      = D8 * H10
    
    if K10 <= H10:
        return K10 * D8
    else:
        return H10 * D8

        



# branch_amount =  275 * loan_amout_break / 10000 + comp.Flat_Fee * branch.commission*  21
def gross_ahf_income(loan_break_amount,comp_plan,ahf_commission_amount):
    """
        ahf gross income commission 
    """
    M9 = 48
    J9 = 19
    
    return   M9*(275 * loan_break_amount.loan_break_point /10000 + comp_plan.Flat_Fee) * 0.3 if M9 <= J9 else   calculate_annual_ahf_income(loan_break_amount,comp_plan,ahf_comission_amount)

def branch_gross_income(loan_break_amount,comp_plan,commission):
    loans_per_year = Branch.objects.all().first().loan_per_year
    annual_cap = AHF.objects.all().first().loan_per_year
    
    
    total_commission = (bps*loan_break_amount.loan_break_point/10000) # 27500
    ahf_commission = total_commission * (1 - commission)
    branch_commission = total_commission * (commission)
    if loans_per_year > annual_cap:
        return annual_cap * branch_commission + total_commission * (loans_per_year - annual_cap)
    else:
        return  loans_per_year * branch_commission
    
                       
                       
 


def get_gci_result(comp_plan,num):
    # const gci_result    = (comp_plan_percentage * 100) * num / 10000  + Number.parseFloat("{{comp_plan_for_lower_limit.Flat_Fee}}")

    return comp_plan.Percentage * 100 * num /10000 + comp_plan.Flat_Fee


def get_percentage():
    break_point = 0.001
    R39 = 0
    S21 = 0
    increment = 0.5
    while R39 > break_point:
        if R39 < 0 :
            S21 = S21 - increment
        else:
            S21 = S21 + increment

balance = float("inf") 
break_point = 0.001   
percentage = 0
increment = 0.5

     

def calculate_balance(branch_gross,total_expense,q22):
    # balance = calculate_balance(branch_gross,total_expense,q22)
    # debit   = branch_gross - calculate_debit(branch_gross,total_expense,q22)
    # diff =  balance - debit
    
    return  branch_gross - calculate_debit(branch_gross,total_expense,q22)



def calculate_total_expense(_branch_commission,_gross_ahf_income):
    """
    O17=IF(N2>=E8*2, SUM(N9:N17),0)
    """
    
    
    total_expense = 0
    categories = Category.objects.all()
    # print("_branch_commission=",_branch_commission)
    # print("_gross_ahf_income=",_gross_ahf_income)
    
    if _branch_commission > 2 * _gross_ahf_income:
        for cat in categories:
            for expense in cat.expense.all():
                total_expense += expense.expense
        return total_expense
    else:
        return total_expense



"""
calculation for table Employee withholding
"""

# def calculate_social_security(loan_break_amount,comp_plan,commission,above_loan_break_point_ahf_commission,percentage,small_percentage):
def calculate_social_security(branch_gross,total_expense,q22):
    """
        Social Security = =IF($N$22<=R24,$N$22*Q24,T24)
        N22 = N20*Q22#({w2_branch_yearly_gross_income_data.w2_Taxable_gross_payroll)
        R24 = 168600 (need to be input) (R24.social_security)
        Q24 = 6.2% (need to be input) (Q24.social_security)
        T24 = Q24*R24  (R24.social_security) (Q24.social_security)
    """
    #15675
    
    N2 = branch_gross
    N20 = N2 -total_expense
    N22 = N20 * q22.value/100
    R24 = BranchPayrollLiabilitieR.objects.all().first().Social_Security
    Q24 = BranchPayrollLiabilitieQ.objects.all().first().Social_Security/100


    if N22 <= R24:
        return N22*Q24
    else:
        return R24 * Q24

def calculate_medicare(branch_gross,total_expense,q22):
    """
    N25 = IF($N$22<=R25,$N$22*Q25,T25+$U$25*($N$22-$R$25))  

    """
    R25 = EmployeeWithholdingR.objects.all().first().Medicare
    Q25 = EmployeeWithholdingQ.objects.all().first().Medicare /100
    U25 = 0.009     #   0.009
    T25 = R25 * Q25 #   2900
    N2 = branch_gross
    N20 = N2 -total_expense
    N22 = N20 * q22.value/100   

   

    # N25=IF($N$22<=R25,$N$22*Q25,T25+$U$25*($N$22-$R$25))
    if N22 <=  R25:
        return N22 * Q25
    else :
        return T25 + U25 * (N22 - R25)
    
    
    
    
    
def calculate_fed_un_employ(branch_gross_income ):
    N22 = (branch_gross_income - 20974) * (0.923199268694749)
    if N22 < 7000:
        return N22 * 0.006
    else:
        return 7000 *  0.006


def calculate_CA_Unemployment(branch_gross,total_expense,q22):
    """
    N34 = $N$22*Q26
    """
    R34 = BranchPayrollLiabilitieR.objects.all().first().CA_Unemployment
    Q34 = BranchPayrollLiabilitieQ.objects.all().first().CA_Unemployment
    T34 = Q34 * R34
    N22 = (branch_gross - total_expense) * q22.value/100,
    Q26 = BranchPayrollLiabilitieQ.objects.all().first().CA_Unemployment

    if R34 >= N22[0]:
        return N22[0] * Q34
    else:
        return T34


def calculate_CA_Disability(branch_gross,total_expense,q22):
    """
    $N$22*Q26
    """
   
    Q26 = EmployeeWithholdingQ.objects.all().first().CA_disability
    N22 = math.ceil(int(branch_gross - total_expense)* q22.value/100),
    return (Q26/100) * N22[0]


def calculate_social_medicare_disability(branch_gross,total_expense,q22):
    return (
        calculate_CA_Disability(branch_gross,total_expense,q22)+
        calculate_medicare(branch_gross,total_expense,q22) +
        calculate_social_security(branch_gross,total_expense,q22)
)



def net_paycheck_for_employee_with_holdings(branch_gross,total_expense,q22,total):
    """
    N28=N22-N27
    """
    
    N2 = branch_gross
    N20 = N2 -total_expense
    N22 = N20 * q22.value/100  
    N27 = calculate_social_medicare_disability(branch_gross,total_expense,q22)
    return N22 - N27


# def calculate_social_security(loan_break_amount,comp_plan,commission,above_loan_break_point_ahf_commission,percentage,small_percentage):
def calculate_social_security_payroll_liabilities(branch_gross,total_expense,q22):
    """
        Social Security = =IF($N$22<=R24,$N$22*Q24,T24)
        N22 = N20*Q22#({w2_branch_yearly_gross_income_data.w2_Taxable_gross_payroll)
        R24 = 168600 (need to be input) (R24.social_security)
        Q24 = 6.2% (need to be input) (Q24.social_security)
        T24 = Q24*R24  (R24.social_security) (Q24.social_security)
    """
    N22 = math.ceil(int(branch_gross - total_expense)* q22.value/100), #w2_branch_yearly_gross_income_data.w2_Taxable_gross_payroll
    R24 = EmployeeWithholdingR.objects.all().first().Social_Security
    Q24 = EmployeeWithholdingQ.objects.all().first().Social_Security
    T24 = (Q24 * R24)
    
    
    R25 = BranchPayrollLiabilitieR.objects.all().first().Medicare
    Q25 = BranchPayrollLiabilitieQ.objects.all().first().Medicare
   
 
    Social_Security = 0
    if R24 >= Q24:
        Social_Security = float(N22[0]) * float(Q24/100)
    else:
        Social_Security = T24
    return Social_Security #branch_gross_income_num - branch_commission * (percentage) * small_percentage


def calculate_medicare_payroll_liabilities(branch_gross,total_expense,q22):
    """
    N25 = IF($N$22<=R25,$N$22*Q25,T25+$U$25*($N$22-$R$25))  
    """
    R25 = EmployeeWithholdingR.objects.all().first().Medicare
    Q25 = EmployeeWithholdingQ.objects.all().first().Medicare
    U25 = (0.9 / 100)
    T25 = R25 * Q25
    N22 = math.ceil(int(branch_gross - total_expense)* q22.value/100),
    
    if (N22[0] <=  R25):
        return (N22[0]) * (Q25 / 100)
    else :
        return (T25 + U25) * (N22[0] - R25)
    
def calculate_ett(branch_gross,total_expense,q22):
    """
    N35 = if N22 <= R35,N22*Q35,T35 
    """
    R35 = BranchPayrollLiabilitieR.objects.all().first().Employment_Training_Tax
    Q35 = BranchPayrollLiabilitieQ.objects.all().first().Employment_Training_Tax/100
    T35 = R35 * Q35
    N22 = (int(branch_gross - total_expense)* q22.value/100)

    if N22 <= R35:
        return N22 * Q35
    else:
        return T35
    

    
    
    
    
    
def calculate_fed_un_employ_payroll_liabilities(branch_gross,total_expense,q22 ):
    """
    N33=IF($N$22<=R33,$N$22*Q33,T33)
    """
    N22 = math.ceil(int(branch_gross - total_expense)* q22.value/100)
    N33 = 0
    R33 = BranchPayrollLiabilitieR.objects.all().first().Fed_Unemploy
    Q33 = BranchPayrollLiabilitieQ.objects.all().first().Fed_Unemploy
    

    if R33 >= N22:
        N33 =  N22 * (Q33/100)
    else:
        N33 = R33 * Q33/100
    return N33


def calculate_CA_Unemployment_payroll_liabilities(branch_gross,total_expense,q22):
    """
    N34=IF($N$22<=R34,$N$22*Q34,T34)
    """
   
    N22 = math.ceil(int(branch_gross - total_expense)* q22.value/100)
    
    R34 = BranchPayrollLiabilitieR.objects.all().first().CA_Unemployment
    Q34 = BranchPayrollLiabilitieQ.objects.all().first().CA_Unemployment / 100
    T34 = R34 * Q34
   
    if N22 <= R34:
        return N22 * Q34
    else:
        return T34
    
def calculate_branch_payroll_liabilities_total(branch_gross,total_expense,q22):
    
    return   calculate_ett(branch_gross,total_expense,q22)+calculate_fed_un_employ_payroll_liabilities(branch_gross,total_expense,q22) + calculate_CA_Unemployment_payroll_liabilities(branch_gross,total_expense,q22)+calculate_medicare(branch_gross,total_expense,q22) +calculate_social_security(branch_gross,total_expense,q22)  

    
def calculate_total_employee_with_holding_expense(branch_gross,total_expense,q22):
    return (branch_gross - total_expense)* q22.value/100



def calculate_debit(branch_gross,total_expense,q22):
    total_employee_with_holding_expense = calculate_total_employee_with_holding_expense(branch_gross,total_expense,q22) 
    branch_payroll_liabilities_total    = calculate_branch_payroll_liabilities_total(branch_gross,total_expense,q22)
    debit = (
            total_employee_with_holding_expense
             + branch_payroll_liabilities_total
             + total_expense
             )
    
    
    return debit 





   
def calculate_gross__new_branch_income(loan_break_amount,comp_plan,gci,value = 275):
    """
        ahf gross income commission 
        K8=IF(K10<=H10,E8*K10,H8+$C8*(K10-H$10))
    """
    branch  = Branch.objects.all().first()
    ahf     = AHF.objects.all().first()   # left side table
    E8      = calculate_above_loan_break_point_ahf_commission(loan_break_amount,comp_plan,branch)
    H8      = E8 * ahf.loan_per_year
    C8      = gci
    K10     = branch.loan_per_year
    H10     = ahf.loan_per_year

    if K10 <= H10:
        return E8 * K10
    else:
        return H8+C8*(K10-H10)
 





    
