#Scott Hansford
#csc110
#section 5
#5/8/18
#simulation loop

#beginning total
rabbit_total = 190
#starting year
year = 1

while year <= 10:
    
    if rabbit_total >= 150:
        rabbit_total -= 100
    #count rabbit total
    rabbit_total *= 2
    #count year
    print('Total rabbits for year', year , 'is: ', rabbit_total)
    year += 1
    
