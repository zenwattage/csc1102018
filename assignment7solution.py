# working_with_lists_SOLUTION.py
#
# One possible solution for this assignment

# CSC 110
# Spring, 2014

# uses a loop to iterate through each element in list 'arr' and create
# a string representation of the list; returns the string 
def to_string(arr):
    if len(arr) == 0:
        return '{}'
    else:
        result = '{$' + format(arr[0], ',.2f')
    for i in range(1, len(arr)):
        result += ', $' + (format(arr[i], ',.2f'))
    return result + '}'
        
# uses a loop to find and return the highest value in list 'arr' 
# assumes the list contains at least one element
def max2(arr):
    highest = arr[0]
    for item in arr:
        if item > highest:
            highest = item
    return highest
    
# uses a loop to find and return the lowest value in list 'arr'
# assumes the list contains at least one element
def min2(arr):
    lowest = arr[0]
    for item in arr:
        if item < lowest:
            lowest = item
    return lowest

#returns the total sales -- the sum of values in the list 'arr'
def total_sales(arr):
    sum = 0
    for item in arr:
        sum += item
    return sum

# returns a new list of values in 'arr' greater than or equal to the threshold
def get_bonus_earners(arr, threshold):
    result = []
    for item in arr:
        if item >= threshold:
            result.append(item)
    return(result)

# user interface
def main():
    sales_list = []
    
    # get and validate sales figures from the user
    # assumes the user always types a number
    amount = float(input('Enter monthly sales for the first division: $'))
    #validate the input
    while amount >= 0:
        sales_list.append(amount)
        amount = float(input('Enter monthly sales for the next \ndivision ' \
                             + 'or a negative number to finish: $'))

    if len(sales_list) == 0:
        print('No sales figures entered; ending the program.')
        return  # this statement terminates the 'main' function

    # get and validate threshold from the user
    # assumes the user always types a number
    threshold = float(input('Please enter a threshold value (>=0): $'))
    while threshold < 0:
        threshold = float(input('Try again -- must be >= 0: $'))

    # show results
    print('\n\nHere is the list of sales figures:')
    print(to_string(sales_list))
    
    print('Sales leader using \'max\':  $' + format(max(sales_list), '.2f'))
    print('Sales leader using \'max2\': $' + format(max2(sales_list), '.2f'))
    
    print('Sales loser using \'min\':   $' + format(min(sales_list), '.2f'))
    print('Sales loser using \'min2\':  $' + format(min2(sales_list), '.2f'))

    total = total_sales(sales_list)
    print('Total sales:   $' + format(total, '.2f'))
    print('Average sales: $' + format(total / len(sales_list), '.2f'))
    print('These sales amounts earn a bonus: ')
    print(get_bonus_earners(sales_list,threshold))

# run the program
main()

# Imagine a set of Documented Test Cases here :-).