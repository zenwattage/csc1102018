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
new_file = 'REPORT-' + user

#lists
years = []
eli_voters = []
reg_voters = []
num_ballots = []

years_total = 0
ballots_total = 0

#OPEN AND READ FILE
infile = open(user,'r')
line = infile.readline().strip('\n')





# while line != '':
#             line = weatherFile.readline()
#             month.append(line)
#             line = weatherFile.readline()
#             num = int(line)
#             total = 0
#             numRain = 0
#             days.append(num)
#             for i in range(num):
#                 line = weatherFile.readline()
#                 temp.append(int(line))
#                 total += int(line) 
#                 line = weatherFile.readline()
#                 if(int(line))== 1:
#                     numRain += 1
#                     rain.append(numRain)
#                     avgTemp.append(total / num)
#             for i in range(len(month)):
#                 print(month[i],end = "")





while line != '':
    year = line
    #assign lines to lists
    #the year line
    year_line = infile.readline().strip('\n')
    years.append(year_line)

    years_total += int(year_line)

    #eligible voters that year
    eli_line = infile.readline().strip('\n')
    eli_voters.append(eli_line)

    #registered voters that year
    reg_voters_line = infile.readline().strip('\n')
    reg_voters.append(reg_voters_line)

    #number of ballots cast that year
    num_ballots_line = infile.readline()
    num_ballots.append(num_ballots_line)



    # print(years)
    # print(eli_voters)
    # print(reg_voters)
    # print(num_ballots)

    #% of registered voters
    # LINE 3 / LINE 2 * 100
    regVoters = (int(reg_voters_line) / int(eli_line))*100
    
    #% who actually voted
    # LINE 4 / LINE 1 * 100
    percVoted = (int(num_ballots_line) / int(eli_line))*100

    #print statement
    #write data lines to file in format:
    #In 1952, 90.81% registered and 72.80% voted.
    print('In '+ year_line +', ' + format(regVoters,'.2f') + '% ' +\
    'registered and ' + format(percVoted,'.2f') + '% ' + 'voted.')
    
    #line = infile.readline()


