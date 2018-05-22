#scott hansford
#csc110
#section 5
#5/18/18

#lab activity - working with files
#this program will ask the user for a file name, read in the numbers from the file,
# and output odds to one evens to another

#get filename from user
filename  = input('What file would you like to open? ')
open_filename = open(filename,'r')
even_file = open('even.txt','w')
odd_file = open('odd.txt','w')

even_sum = 0
count_neg = 0
read_string = open_filename.readline()

while read_string != '':
    
    num = int(read_string)

    if num % 2 == 0:
        even_sum += num
        even_file.write(str(num) + '\n')

    if num < 0 :
        count_neg += 1

    else:
        odd_file.write(str(num) + '\n')
    read_string = open_filename.readline()
    
print('The sum of even numbers is: ', even_sum )
print('The negative count is: ', count_neg)

#close files
open_filename.close()
even_file.close()
odd_file.close()