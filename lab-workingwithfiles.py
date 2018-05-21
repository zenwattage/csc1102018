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

    #while loop
    while read_file != '':
        
    #open and read from file
    if filename != '':
        open_file = open(filename,'r')
    elif filename == '':
        print('This file is empty. Please open a valid file.')
        filename = str(input('What file would you like to open? '))
    #read file one line at a timee
    
    line1 = str(open_file.readline())
    print(line1)
    even_file = open('even.txt','w')
    odd_file = open('odd.txt','w')
    
    for i in line1:
        if line1 % 2 == 0:
            line1 = even

    even =even_file.write()
    odd = odd_file.write()

    
    

# def evenodd(line):
#     linetest = line
#     even_file = open('even.txt','w')
#     odd_file = open('odd.txt','w')
#     if str(linetest) % 2 != 0:
#         odd_file.write(str(linetest))
#     elif str(linetest) % 3 != 0:
#         even_file.write(str(linetest))
#     even_file.close()
#     odd_file.close()
    



    
    





    


#display the sum of the even numbers and the count of the negative numbers

#input section

#read file
    #close the file
    print('Data written to: ',odd_file, 'and', even_file)

#call main function
main()