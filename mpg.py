# Program to calculate gas mileage in "miles per gallon"
# based on distance traveled and gallons used.
#
# mpg = miles/gallons
#
# CSC 110
# 9/25/11

print('This program will calculate mpg based on your input')
print()
print()

# input section (The input() and float() functions are covered in Section 2.6.)
miles = float(input('How many miles did you travel? '))
gallons = float(input('How many gallons did you use? '))

# processing
mpg = miles / gallons 

#output section
print('You travelled', miles, 'miles')
print('You used', gallons, 'gallons')
print('Your mpg = ', mpg)

# Read Section 2.8 to see how you can format the output more nicely.
