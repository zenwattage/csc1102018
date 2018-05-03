##num = int(input('Enter a number: '))
##while num <= 5:
##    print(num)
##    num = num + 1
##print('Done')
##        

##count = 4
##num = int(input('Enter a number: '))
##while count <= num:
##    print(count)
##    count = count + 2
##print('Done')

##count = 4
##num = int(input('Enter a number: '))
##while count <= num:
##    count = count + 2
##    print(count)
##print('Done')

##count = 4
##num = int(input('Enter a number: '))
##for count in range(num):
##    print(count)
##print('Done')

##found = False
##num = int(input('Enter a number: '))
##for count in range(1, num, 2):
##    print(count)
##    if count == 5:
##        found = True
##print(found)

found = False
num = int(input('Enter a number: '))
for count in [6, 5, 9, 2, 8]:
    if num == count:
        found = True
    else:
        print(count)
print(found)
