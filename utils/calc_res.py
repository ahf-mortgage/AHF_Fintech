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

