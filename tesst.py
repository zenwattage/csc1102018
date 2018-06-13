# what_name_you_want = print("yo yo yo ")

# print(what_name_you_want)


# a = 'record'
# b = 1
# c = a[b]
# d = c in 'test'

# print(c)

# test = 'this is a test'
# result = 'A'
# count = len(test)
# while count > 0:
#     count -= 2
#     result += test[count]
# print(result)


# s = 'hello everyone go fuck yourselves'
# for ch in s:
#     print(ch)


# s = 'test'
# a = 'a' in s
# b = s in 'e'

# distance = [4.5,7.1,8.9,3.2]
# sum = 0
# for i in distance:
#     sum = sum + i
# print(sum)

# distance = [4.5,7.1,8.9,3.2]
# sum = 0
# for i in range(0,len(distance)):
#     sum = sum + i
# print(sum)

# distance = [4.5,7.1,8.9,3.2]
# sum = 0
# for i in range(0,len(distance)):
#     sum = sum + distance[i]
# print(sum)

# distance = [4.5,7.1,8.9,3.2]
# sum = 0
# for i in range(1,len(distance)):
#     sum = sum + distance[i]
# print(sum)

# distance = [4.5,7.1,8.9,3.2]
# sum = 0
# for i in range(1,len(distance)):
#     sum = sum + distance[i]
#     print(sum)

# price = [25,10,15,20]
# for i in range(len(price)):
#     price[i] = price[i] * 1.1
# for i in range(len(price)):
#     print(price[i])

# splitTest = 'Hello everyone shit the bed!'
# new = splitTest.split(' ')
# print(new)
import operator
distance = [4.5,7.1,8.9,3.2]

first = float(distance[0])
second = float(distance[1])
third = float(distance[2])
fourth = float(distance[3])

front_two = sum(first,second)
middle_two = sum(second,third)
back_two = sum(third,fourth)
map(operator.add,first,second)
print('The front two are:',front_two,'\nThe middle two are: ',middle_two, '\nThe back two are: ',back_two)