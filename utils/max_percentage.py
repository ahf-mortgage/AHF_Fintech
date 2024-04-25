

def get_percentage_recurssion():
    balance = float("inf") 
    break_point = 0.001   
    percentage = 0
    increment = 0.5

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
        
        
print(get_percentage_recurssion())
        
        
