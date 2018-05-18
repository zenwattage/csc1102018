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
    print(''*5)
    
    user_savings = int(input('Enter annual savings (at least $100): $'))
    print('Retirement Savings Table:')    
    print('' * 5)    
    print('Starting' + (' ' * 10) + 'Assumed Interest Rate' )    
    print('  Age' + ' '*10 + str(starting_rate) + '%'\
         + ' '*10 + str(starting_rate + 2) + '%'\
         + ' '*10 + str(starting_rate + 4) + '%'\
         + ' '*10 + str(starting_rate + 6) + '%')


    #main loop 
    while user_savings > 100 and starting_age < 70:
        second_rate = 0
        second_balance = 0
        third_rate = 0
        third_balance = 0
        fourth_rate = 0
        fourth_balance = 0           
        for i in range(1,10):

            second_rate += starting_rate + 2
            second_balance += user_savings
            # print(starting_age,' $',format(calc_final_balance\
            # (starting_age,second_balance,second_rate),'.2f'))
            
            third_rate += second_rate + 2
            third_balance += second_balance
            
            # print(starting_age,' $',format(calc_final_balance\
            # (starting_age,third_balance,third_rate),'.2f'))
            
            fourth_rate += third_rate + 2
            fourth_balance += third_balance
            # print(starting_age,' $',format(calc_final_balance\
            # (starting_age,fourth_balance,fourth_rate),'.2f')) 
            
            print(starting_age, ' $', format(calc_final_balance\
            (starting_age,user_savings,starting_rate),'.2f'),\
            ' $',format(calc_final_balance(starting_age,second_balance,second_rate),'.2f'),\
            ' $',format(calc_final_balance(starting_age,third_balance,third_rate),'.2f'),\
            ' $',format(calc_final_balance(starting_age,fourth_balance,fourth_rate),'.2f'))
            starting_age += 5
    
        
    
    print(' ')
    print('When are YOU going to start saving for retirement?')
    print(' ')


    #Input validation & Error message
    while user_savings < 100 :
        print("Sorry savings must be greater than $100. Please try again: ")
        user_savings = int(input('Enter annual savings (at least $100): $'))



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


#call main function
main()