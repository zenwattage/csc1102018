# Code developed in class on Thursday, 5/24
# Demonstrates a series of LIST ALGORITHMS

# CSC 110


##############################
# Function definitions section

# Returns the sum of all the numbers in arr
# that are less than or equal to 20.
# arr must contain only numbers.
def sum_lte_20(arr):
    total = 0
    for num in arr:
        if num <= 20:
            total += num
    return total

# CHANGES the list arr by adding 2 to each element value.
# arr must contain only numbers.
def plus2(arr):
    for i in range(len(arr)):
        arr[i] += 2

# Returns the highest value in arr.
# len(arr) must be > 0
# All items in arr must be "comparable" to each other
# (e.g. all numbers, or all strings).
def get_highest(arr):
    highest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > highest:
            highest = arr[i]
    return highest

# Returns True if the target value is found in arr;
# False otherwise.
def contains(arr, target):
    result = False
    for x in arr:
        if x == target:
            result = True
    return result

# Returns True if the target value is found in arr;
# False otherwise.
def contains2(arr, target):
    for x in arr:
        if x == target:
            return True
    return False

# Returns the INDEX of the FIRST occurrence of the
# target value in arr, or -1 if not found.
def index_of(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Returns a NEW LIST containing all values from arr
# that are greater than the threshold.
# Each element in arr must be "comparable" to the threshold.
def larger_than(arr, threshold):
    result = []
    for num in arr:
        if num > threshold:
            result.append(num)
    return result

# Main program -- contains code to TEST the functions above.
def main():
    nums = [5, 12, -2, 18, 25]
    test = [5, 10, 15]
    answer = sum_lte_20(nums)
    print(answer)
    print(test)
    plus2(test)
    print(test)
    print('highest (first):', get_highest([99, 34, 98, 17, 40]))
    print('highest (middle):', get_highest([98, 34, 99, 17, 40]))
    print('highest (last):', get_highest([92, 34, 98, 17, 99]))

    print(nums)
    print('contains 5 (first):', contains(nums, 5))
    print('contains 18 (middle):', contains(nums, 18))
    print('contains 25 (last):', contains(nums, 25))
    print('contains 13 (not present):', contains(nums, 13))
    print('contains2 5 (first):', contains2(nums, 5))
    print('contains2 18 (middle):', contains2(nums, 18))
    print('contains2 25 (last):', contains2(nums, 25))
    print('contains2 13 (not present):', contains2(nums, 13))
    print('index_of 5 (first):', index_of(nums, 5))
    print('index_of 18 (middle):', index_of(nums, 18))
    print('index_of 25 (last):', index_of(nums, 25))
    print('index_of 13 (not present):', index_of(nums, 13))
    print(nums)
    print('larger_than -3 (all):', larger_than(nums, -3))
    print('larger_than 11 (some):', larger_than(nums, 11))
    print('larger_than 25 (none):', larger_than(nums, 25))
    print(nums)

main()