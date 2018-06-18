# def get_pairs(arr):
#     result = []
#     for i in range(len(arr) - 1):
#         result.append(arr[i] + arr[i + 1])
#     return result

# shit = [3,4,5,6]

# print(get_pairs(shit))

# def swap_first_last(arr):
#     temp = [-1:] + temp[1:-1] + temp[:1]
#     return temp

# turn = [2,3,4,5]
# print(swap_first_last(turn))

# nums = [1,2,3,4,5]
# word = 'farts'

# for i in range(len(nums)):
#     print(nums[i])
    

# total = 3
# for bit in range(-4, 11, 3):
#     if bit > 0 and bit < 7:
#         total = total + bit
#     else:
#         print(total)
#         total = total - bit
# print(bit)

# word = 'strand'
# result = '>'
# for i in range(len(word)):
#     if word[i] in 'ds':
#         result += word[i] + str(i)
# print(result + '<')


nums = [3,4,5,6]
for i in range(1,len(nums)):
    nums[i] = nums[i] + nums[i-1]
    print(nums[i])
print(nums)