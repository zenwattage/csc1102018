#Scott Hansford
#csc1102018
#section 5
#5/22/18
#Assignment #6 - Vote Participation Data
#This program will ask the user for a file name. Open that file then
#open a new 'REPORT' file then write a report into that file.

#get file to open from uread_file
user = input('Enter the name of your data file: ')

#open file
read_file = open(user,'r')

#make new file named 'REPORT-'
new_file = 'REPORT-' + user
out_file = open(new_file,'w')

#read first 4 lines into appropriate variables
YEARS = read_file.readline()
ELIG_VOTERS = read_file.readline()
REG_VOTERS = read_file.readline()
BALLOTS_CAST = read_file.readline()

#counters
total_years = 0
total_ballots = 0
total_reg_voters = 0
lessThan = 0
moreThan = 0


while YEARS != '':
    #convert lines to integers
    year_line = int(YEARS)
    eligVoters = int(ELIG_VOTERS)
    regVoters = int(REG_VOTERS)
    ballots = int(BALLOTS_CAST)
    
    #% of registered voters
    # LINE 3 / LINE 2 * 100
    percRegVoters = (regVoters / eligVoters) * 100
    
    #% who actually voted
    # LINE 4 / LINE 1 * 100
    percVoted = (ballots / eligVoters)*100

    #print statement
    #write data lines to file in format:
    #In 1952, 90.81% registered and 72.80% voted.
    out_file.write('In '+ str(year_line) +', ' + format(percRegVoters,'.2f') + '% ' +\
    'registered and ' + format(percVoted,'.2f') + '% ' + 'voted.\n')

    #accumulators
    total_years += 1
    total_ballots += ballots
    total_reg_voters += percRegVoters

    #DISPLAY TO USER IN SHELL
    #total % of registered voters
    totalPercRegVotes = (ballots / regVoters) * 100


    # number of years with less than 60% of registered voters casting ballots
    if totalPercRegVotes < 60:
        lessThan += 1

    # percentage of years with more than 80% of reg. voters casting ballots
    if totalPercRegVotes > 80:
        moreThan += 1

    #LOOP TO NEXT LINE 
    YEARS = read_file.readline()
    ELIG_VOTERS = read_file.readline()
    REG_VOTERS = read_file.readline()
    BALLOTS_CAST = read_file.readline()

avgRegVoter = total_reg_voters / total_years
percMoreThan = (moreThan / total_years) * 100

# display in shell to user:
# The total number of years listed: 17
print('The total number of years listed: ' + str(total_years) + '\n')
# Total ballots cast in all these years: 34,436,792
print('Total ballots cast in all these years: ' + format(total_ballots,'.0f') + '\n')
# Average percentage of eligible voters registered: 79.55%
print('Average percentage of eligible voters registered: ' + format(avgRegVoter,'.2f') + '%\n')
# Number of years with less than 60% of registered voters casting ballots: 0
print('Number of years with less than 60% of registered voters casting ballots: ' + str(lessThan) + '\n')
# Percentage of years with more than 80% of registered voters casting ballots: 47.1%
print('Percentage of years with more than 80% of registered voters casting ballots: ' + format(moreThan,'.1f') + '%\n')
# An output file named REPORT-PresidentialElections.txt has been created.
print('An output file named ' + new_file + ' has been created.')

#close files
out_file.close()
read_file.close()