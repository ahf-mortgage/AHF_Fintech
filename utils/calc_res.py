#ahf_annual_amount = (((271(constant))*(loan_break_amount)/10000+comp_plan.Flat_plan)* ahf_comission_amount) *  21(constant)


def calculate_annual_ahf_income(loan_break_amount,comp_plan,ahf_comission_amount):
    """
       annual income commission 
    """
    print(loan_break_amount.loan_break_point ," loan_break_amount.loan_break_point ", comp_plan.Flat_Fee,"  comp_plan.Flat_Fee ",ahf_comission_amount," ahf_comission_amount")
    return( (275 * loan_break_amount.loan_break_point )/ 10000 + comp_plan.Flat_Fee )* ahf_comission_amount * 21


# branch_amount =  275 * loan_amout_break / 10000 + comp.Flat_Fee * branch.commission*  21
def calculate_gross_ahf_income(loan_break_amount,comp_plan,commission):
    """
        ahf gross income commission 
    """
    return ((275 * loan_break_amount.loan_break_point )/ 10000 + comp_plan.Flat_Fee )* commission * 21



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
    return ((275 * loan_break_amount.loan_break_point )/ 10000 + comp_plan.Flat_Fee )  * 48



def get_gci_result(comp_plan,num):
    return comp_plan.Percentage * 100 * num /10000 + comp_plan.Flat_Fee


# s1 = m9

    
