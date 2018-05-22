#scott hansford
#csc110
#section 5
#5/18/18

#lab activity - working with files
#this program will ask the user for a file name, read in the numbers from the file,
# and output odds to one evens to another
def main():
    #get filename from user
    filename  = str(input('What file would you like to open? '))
    open_filename = open(filename,'r')
    read_file = open_filename.readline()
    read_string = str(read_file)
    print(read_string)


    while read_string != '':
    
        even_sum = 0
        count_neg = 0
        even_file = open('even.txt','w')
        odd_file = open('odd.txt','w')
        #even_file.write(str(read_file))


        if read_string % 2 == 0:
            even_sum += 1
            even_file.write()

        elif read_string <= 0 :
            count_neg += 1

        else:
            odd_file.write(read_string)
        
    print(read_file)
    open_filename.close()
    even_file.close()
    odd_file.close()

main()