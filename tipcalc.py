#Scott Hansford
#CSC110
#Section5
#4/7/2018

#Tip Calculator

print("****"*10)
print()
print("Hello! Welcome To The Tip Calculator!")
print()

#get bill and tip amount from user
user_bill = input("How much is the dollar amount of the bill? ")

user_tip = input("How much percent would you like to tip? ")

#convert inputs to floats
bill = float(user_bill)
tip = float(user_tip)

#convert tip amount to percent
tipPercent = tip/100

#calculate tip amount
tipAmount = tipPercent*bill

#calculate total bill amount w/ tip
billTotal = tipAmount + bill

#format tip and bill
finalTip = format(tipAmount,'.2f')
finalBill = format(billTotal,'.2f')

#Output results
print("Your desired tip amount is: $", finalTip)

print("Your total bill, including tip, is: $", finalBill)

#Tip amount dependant message:
if tip > 20:
    print("You are very generous!")
if tip < 20:
    print("You are a cheap bastard!")
