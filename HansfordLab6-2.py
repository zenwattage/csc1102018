#Scott Hansford
#CSC110
#Lab 6-2
answer = "y"
while answer == "y":
    num = int(input("Please input an integer: "))
    sum_num = 0

    while num > 0:
          remainder = num % 10
          sum_num = sum_num + remainder
          num = num //10
    print(sum_num)
    answer = input("Would you like to continue? y/n? ")
