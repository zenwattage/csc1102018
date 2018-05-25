# Code SIMILAR TO that in class on Tuesday, 5/22
# Demonstrates some basic list operations

# CSC 110

def main():
    nums = [5, 12, -2, 18, 25]
    colors = ['red', 'green', 'blue']
    by_fives = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

    print(nums)
    print('Length of nums:', len(nums))
    print('nums[2]:', nums[2])
    print('Type of nums:', type(nums))
    print('Type of nums[2]:', type(nums[2]))

    print()
    print(colors)
    print('Length of colors:', len(colors))
    print('colors[2]:', colors[2])
    print('Type of colors:', type(colors))
    print('Type of colors[2]:', type(colors[2]))

    # lists are MUTABLE -- let's change nums
    print('\nnums before and after being changed:')
    print(nums)
    nums[2] = 6
    print(nums)

    # a BASIC 'for' loop to access list items
    print('\nExamining each value in a list:')
    for n in nums:
        print(n)
    print()
    for c in colors:
        print(c)

    # an INDEXED loop using a 'for' statement
    print('\nExamining values using an INDEXED loop:')
    for i in range(len(nums)):
        print(i, nums[i])
    print()
    for i in range(len(colors)):
        print(i, colors[i])
    print()
    for i in range(9, 0, -2):
        print(by_fives[i])

    # an INDEXED loop using a 'while' statement
    print()
    i = 0
    while i < len(nums):
        print(i, nums[i])
        i += 1

    # sum, min, max -- built-in functions 
    print('\nsum, min, max:')
    print(nums)
    print(by_fives)
    print('sum(nums):', sum(nums))
    print('sum(by_fives):', sum(by_fives))
    print('min(nums):', min(nums))
    print('max(nums):', max(nums))

    # A VARIATION on the "sum" algorithm:
    # Determine the sum of all the numbers in nums
    # EXCEPT ignore numbers < 10.
    total = 0
    for num in nums:
        if num >= 10:
            total += num
    print(total)



main()