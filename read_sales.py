
#example from 

#this program reads all the values in
# the sales.txt file.

def main():
    #open the sales.txt file for reading
    sales_file = open('sales.txt','r')
    
    # read the firstline from the file, but
    #don't convert to a number yet. We still 
    #need to test for an empty string
    line = sales_file.readline()

    #as long as an empty stirng is not returned
    # from readline, contineue processing
    while line != '':
        #convert line to a float
        amount = float(line)

        #format and display the amount
        print(format(amount,'.2f'))

        #read the next line
        line = sales_file.readline()
    sales_file.close()
#call the main function
main()