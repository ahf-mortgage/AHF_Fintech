from .calc_res import calculate_balance


def automate_q22_value(branch_gross,total_expense,q22):
    q22.value = 98
    balance = calculate_balance(branch_gross,total_expense,q22)
   
    increment = 1
    j  = 0
   
  
    while abs(balance) > 0.001 and j < 60:
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
        while balance > 0 and i < 10:
            q22.value = q22.value + increment
            # increment = 
            # print("increment= ",increment)
            balance = calculate_balance(branch_gross,total_expense,q22)

            print("incrementc= ",increment)
            print("q22c= ",q22.value)
            print("balance ",balance)

            i = i + 1
            
        # balance is still too low, need to raise to q22
        k = 0
        while balance > 0 and k < 10:
            increment = increment /10
            print("incrementK= ",increment)
            q22.value = q22.value + increment
            balance = calculate_balance(branch_gross,total_expense,q22)
            print("incrementK= ",increment)
            print("q22c= ",q22.value)
            print("balance ",balance)
            k = k + 1
            # balance is too low we need to increase q22 
            print("++++++++++++++++++++++++++++++++++++++++++++++")
            
            
        # balance is too high,need to lower q22
        i = 0
        while balance < 0 and i < 160:
            q22.value = q22.value - increment + increment/2
            increment = increment / 10
            print("incrementd= ",increment)
            balance = calculate_balance(branch_gross,total_expense,q22)
            print("q22 ",q22.value)
            print("balance ",balance)
            i = i + 1
        
        
        # balance is still too high , need to lower q22 by current increment
        p = 0 
        while balance < 0 and p < 160:
            q22.value = q22.value - increment
            balance = calculate_balance(branch_gross,total_expense,q22)

            print("incremente= ",increment)
            print("q22d= ",q22.value)
            print("balance ",balance)

            p = p + 1
        j = j + 1
      



    j = 0
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