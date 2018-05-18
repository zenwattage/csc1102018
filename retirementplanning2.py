

def calc_final_balance(age, saved, percentage):
    time_left = 70 - age # get the number of years left
    balance = 0
    percentage = float(percentage) / 100 # percentage division
    percentage += 1
    for _ in range(time_left): # loop to go through each year
        balance += saved
        balance *= percentage # get the interest, and multiply it to percentage
    return balance # return the amount

print (calc_final_balance( 65, 2000, 10 ))
print('$' + format(calc_final_balance( 30, 3000, 6 ), '.2f'))
print('$' + format(calc_final_balance( 20, 2000, 5.5 ), '.2f'))