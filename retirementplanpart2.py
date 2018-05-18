#Scott Hansford
#csc110
#section 5
#5/15/2018
#Assignment 5 - Retirement planning 2

#This program will ask the user how much they want to save,/
# then generate a retirement planning table based on that input.

#main function will get a savings amount from user, pass that amount,
#to the calc_final_balance() function, 
#then display a table that shows what the amount would return,
#at 4,6,8,10% interest rates, in 5 year increments, from 20 - 65.
def main():
    starting_rate = 4
    starting_age = 20
    print('Welcome to the retirement planning tool!')
    user_savings = int(input('Enter annual savings (at least $100): $'))
    print('Retirement Savings Table:')
    print('Starting')
    print(starting_age, str(starting_rate) + '%')
    print('Current balance = $'+ format(calc_final_balance(starting_age, user_savings, starting_rate),'.2f'))
#print('Remaining balance = $' + format(balance, ',.2f') + '.')

#




#function to calculate the amount saved, at a certain rate, over a # of years
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

main()