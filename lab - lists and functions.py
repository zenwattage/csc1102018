#scott hansford
#csc1102018
#section 5
#5/24/18
#lab - lists and functions

#first function: swap
#def function test
yourlist = [10, 20, 30, 40]

#This function will 'swap'values
def swap_first_last(somelist):
    first = somelist[0:]
    last = somelist[:-1]

    while first < last:
        update = somelist[first]
        somelist[first] = somelist[last]
        somelist[last] = update
        
    return somelist
    #new_order = first[0], stuff[-1] = last[-1], first[0]
    
list_swap = swap_first_last(yourlist)

print(list_swap)
