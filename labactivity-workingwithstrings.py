#Scott Hansford
#csc110
#section 5
#5/30/2018
#Lab activity - Working with Strings

#write a counting loop that prints out 5,4,3,2,1,0,-1,-2,-3
#each number on seperate line
#

#COUNT DOWN FROM 5 TO -3
# count = 0
# while count > -4:
#     print(count)
#     count -= 1

# for num in range(5,-4,-1):
#     print(num)

# 1. Use a loop to print user's phrase one character per line
#get phrase from user
user_phrase = input('Enter a phrase: ')
#print users phrase one character per line
read_phrase = user_phrase

# for i in read_phrase:
#     print(i + '\n')


# 2.print phrase all on one line in reverse order
# #reverse string
# def reversed_string(aString):
#     return aString[::-1]

# print(reversed_string(read_phrase))


# 3.
#  print original phrase in reverse order, all on one line, again
# but this time WITHOUT using a slice or 'reverse()' - instead use
# a loop to print one character at a  time, all on the same line, but
# in reverse order.
# remember: you can use 'end' to keep all characters on same line
def reverse(p):
    string = ''
    for i in p:
        string = i + string
    return string
#call reverse function
print(reverse(read_phrase))


# 4.
# print the phrase one word per line
def one_per_line(line):
    phrase = line
    for words in phrase:
        if words == ' ':
            print('')
        else:
            print(words, end = '')

one_per_line(read_phrase)


# 5.
# 
