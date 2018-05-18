#Scott Hansford
#csc110
#Section 5
#5/10/2018
#Retirement Planning, Part 1

# P = r/t
 
# calculate interest on current balance: amount*rate =  
# add interest to current balance: amount + rate
# count up 1 year from starting age until you get to 70


#main retirement function

#function that calculates the final balance in a retirement account
# after annual savings accrue for and earn interest for a number of years.

def calc_final_balance(age,balance,rate):
  ### Simulate account changes until the account is paid in full

  amount = balance          # initialize accumulator
  age = age                # initialize counter
  rate = rate        # initialize accumulator;
  #convert rate to percent
  interest = rate/100

# NOTICE that the loop continues as long as the balance is greater than
# zero, BUT not longer than 1200 months -- a condition necessary
# to prevent an infinite loop if the payment is too low.
  
  year_return = 0


  while age < 70:
    year_return = amount + (amount * interest)
    age += 1

    print(year_return)
  
  if age == 70:
    print(year_return)

print('$' + format(calc_final_balance( 30, 3000, 6 ), '.2f'))
print('$' + format(calc_final_balance( 20, 2000, 5.5 ), '.2f'))
print('$' + format(calc_final_balance( 65, 2000, 10 ), '.2f'))
# The function requires 3 parameters: 
# the starting age for saving,

# the amount saved each year,

# and the percentage interest rate. 


# This function may assume that the values have been previously validated 
# -- no input validation is needed in this function.
# Saving is assumed to stop at age 70.
# The function uses a loop to perform a simulation of retirement savings. 
# The loop iterates one time for each year that savings occur. 

# Each year, the account balance is increased by the amount saved each year,
# and then -- after this increase -- the account earns one year's interest.
# The function should return the final balance at age 70. """

""" TEST the 'calcFinalBalance' function by adding statements in the 'main program' to
 print out the final balance for several test cases and confirm that it is correct.
  For example, these statements:

print('$' + format(calc_final_balance( 30, 3000, 6 ), '.2f'))
print('$' + format(calc_final_balance( 20, 2000, 5.5 ), '.2f'))

should write on the web page the results $492143.05 and $519518.88. 
Choose test cases that check the function thoroughly, and document your testing in comments.

Here is a simple test case you can more easily trace by hand: 
calc_final_balance( 65, 2000, 10 ) should return the value 13431.22. """

"""
 /10 function definition including simulation loop
/5 documented test cases 
/5 proper comments; good variable names; indenting; blank lines """