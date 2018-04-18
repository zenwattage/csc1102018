def show_message():
    print("Welcome to the updated tip calculator.")
    print("This program will show you several options for a tip amount.")
    print()

def show_tip(a,b):
    tip = float(b/100)
    print("A",b , "% tip on a $",a,"bill amounts to", format(a * tip,'.2f'))
    

def main():
    show_message()
    
    bill_amount = float(input('Please enter the amount of the bill: $'))

    show_tip(bill_amount, 15)
    print()
    show_tip(bill_amount, 18)
    print()
    show_tip(bill_amount, 20)
    print()
    show_tip(bill_amount, 25)

#start the program
main()


##Welcome to the updated tip calculator.
##This program will show you several options for a tip amount.
##
##Please enter the amount of the bill: $20
##
##A 15% tip on a $20.00 bill amounts to $3.00.
##
##A 18% tip on a $20.00 bill amounts to $3.60.
##
##A 20% tip on a $20.00 bill amounts to $4.00.
##
##A 25% tip on a $20.00 bill amounts to $5.00.
