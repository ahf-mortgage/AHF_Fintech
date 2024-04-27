
from recruiter.models import Bps,Branch
bps = Bps.objects.all().first().bps

def calculate_annual_ahf_income(loan_break_amount,comp_plan,ahf_comission_amount):
    """
       annual income commission 
    """
    return( (275 * loan_break_amount.loan_break_point )/ 10000 + comp_plan.Flat_Fee )* ahf_comission_amount * 21


# branch_amount =  275 * loan_amout_break / 10000 + comp.Flat_Fee * branch.commission*  21
from recruiter.models import AHF
def calculate_gross_ahf_income(loan_break_amount,comp_plan,commission,value = 275):
    """
        ahf gross income commission 
    """
    
    
    # return ((275 * loan_break_amount.loan_break_point )/ 10000 + comp_plan.Flat_Fee )* commission 
    # return loan_break_amount.loan_break_point * commission
    
    # (275(need to be input variable)*loans_break_amount/10000+ Flat_fee) * branch_commission_spilit * loans_per_year
    loans_per_year = AHF.objects.all().first().loan_per_year
    return  ((value * loan_break_amount.loan_break_point )/ 10000 + comp_plan.Flat_Fee)* commission * loans_per_year
    



# branch_amount =  275 * loan_amout_break / 10000 + comp.Flat_Fee * branch.commission*  21

def gross_ahf_income(loan_break_amount,comp_plan,ahf_comission_amount):
    """
        ahf gross income commission 
    """
    M9 = 48
    J9 = 19
    
    #IF(M9<=J9,M9*F7,I7)
    return   M9*(275 * loan_break_amount.loan_break_point /10000 + comp_plan.Flat_Fee) * 0.3 if M9 <= J9 else   calculate_annual_ahf_income(loan_break_amount,comp_plan,ahf_comission_amount)

def branch_gross_income(loan_break_amount,comp_plan,commission):
     #275 *  loan_amount_break. loan_amount_break/10000 + comp_plan.Flat_FEE  * M9
    # return ((275 * loan_break_amount.loan_break_point )/ 10000 + comp_plan.Flat_Fee )  * 48
    loans_per_year = Branch.objects.all().first().loan_per_year
    annual_cap = AHF.objects.all().first().loan_per_year
    
    
    total_commission = (bps*loan_break_amount.loan_break_point/10000) # 27500
    ahf_commission = total_commission * (1 - commission)
    branch_commission = total_commission * (commission)
    if loans_per_year > annual_cap:
        return annual_cap * branch_commission + total_commission * (loans_per_year - annual_cap)
    else:
        return loans_per_year * branch_commission 
    
                       
                       
    # if branch_loans_per_year > annual_cap:  
    #     return (bps*loan_break_amount.loan_break_point/10000) * (branch_loans_per_year - annual_cap)  + annual_cap * (bps*loan_break_amount.loan_break_point/10000)*commission 
    # else:
    #      return (bps*loan_break_amount.loan_break_point/10000)*commission * branch_loans_per_year 



def get_gci_result(comp_plan,num):
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

     
def get_percentage_recurssion():
    if balance < break_point:
        return percentage
    if balance < 0:#if R39 is negative then S21 = S21 - increment
        increment = increment/10
        percentage -= increment
        get_percentage_recurssion()
        
    else:
        increment = increment/ 10
        percentage += increment
        get_percentage_recurssion()
        
    



from W2branchYearlyGross.models import Category
def calcalate_total_expense():
    total_expense = 0
    categories = Category.objects.all()
    for cat in categories:
        for expense in cat.expense.all():
            total_expense += expense.expense

    return total_expense

    

# s1 = m9
# S1 = M9 Number of loans
# P1 = M7 Branch Yearly Gross Revenue
# P19  =P1-Q16 Net income before payroll
# P17 =SUM(P8:P16) Total expenses
# P21 =P19*S21   Taxable gross payroll
# O23 = label(social security  Employee) = P23
# 030 = label(socail security Branch)  = P30
# S21 = 96.205%  iterate to get this value so that balance is less than 0.001
# R39 = P39 - Q39 
# while R39 is greater than 0.001 iterate S21 
        # if R39 is negative then S21 = S21 - increment
        # else S21 = S21 + increment
        # adjust increment
        # S1 = 96.205324% final solution balance equals 0.00
        # S1 = 96.0 balance equals -11.02 minus sign tells you 96.0 is too big 
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
        

    
