#Scott Hansford
#csc110
#section 5
#5/10/2018
#retirement planning simulation

def calc_final_balance(age, amount_saved, int_rate):
    #subtract age at start from 70 for number of iterations
    year = 70 - age
    
    #count accrued balance
    new_balance = 0
    
    #divide rate/100 to convert rate to a percent(& float)
    int_rate = float(int_rate)/100
   
    #count interest
    int_rate += 1
    
    #iterate once every year
    for i in range(year):
        year += 1        
        new_balance += amount_saved 
        new_balance *= int_rate
    return new_balance

#test cases
# (30, 3000, 6) correct return should be: $492143.05. Working correctly.
print('$' + format(calc_final_balance( 30, 3000, 6 ), '.2f'))
# (20, 2000, 5.5 ) correct return should be: $519518.88. Working correctly.
print('$' + format(calc_final_balance( 20, 2000, 5.5 ), '.2f'))
# (65, 2000, 10) correct return should $: 13431.22. working correctly.
print('$' + format(calc_final_balance( 65, 2000, 10 ),'.2f'))