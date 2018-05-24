#Scott Hansford
#csc1102018
#section 5
#5/22/18
#Assignment #6 - Vote Participation Data
#This program will ask the user for a file name. Open that file then
#open a new 'REPORT' file then write a report into that file.



# Final report:
# Total number of years listed
# years_total = 0
# Total number of ballots cast in all years
# ballots_total = 0
# average % of eligible voters who registered
# 
# number of years with less than 60% of registered voters casting ballots
# percentage of years with more than 80% of reg. voters casting ballots
# name of report file

# The total number of years listed: 17
# Total ballots cast in all these years: 34,436,792
# Average percentage of eligible voters registered: 79.55%
# Number of years with less than 60% of registered voters casting ballots: 0
# Percentage of years with more than 80% of registered voters casting ballots: 47.1%
# An output file named REPORT-PresidentialElections.txt has been created.



#get file to open from user
user = input('Enter the name of your data file: ')

#open and read the file
infile = open(user,'r')
line = infile.readline()
new_file = 'REPORT-' + user

while line != '':
    num = int(line)
    #open 'REPORT-' file
    print(num)
    open_new = open(new_file,'w')
    if num < 5:
        open_new.write(str(num)+'\n')
        num +=1
        print(num)


    
    

    #write data lines to file in format:
    #In 1952, 90.81% registered and 72.80% voted.
    

    # % of registered voters
    # LINE 3 / LINE 2 * 100

    # % voted
    # LINE 4 / LINE 1 * 100


  


    #line = infile.readline()


