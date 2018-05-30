#INPUT

files_name = input('Enter the name of file (PresidentialElections.txt or MidTermElections.txt): ')

# PROCESSING

# OPEN USER'S INPUT FILE AND CREATE OUTPUTFILE

users_file = open(files_name, 'r')
outfilename = 'REPORT-' + files_name
outfile = open(outfilename, 'w')

#INITILIZATION

# Determines the first year, # eligible voters, # registered voters, # of ballots

years = users_file.readline()

eligible_voters = users_file.readline()

registered_voters = users_file.readline()

ballots_cast = users_file.readline()


# COUNTERS & BEGINNING VALUES

tot_years = 0
tot_ballots = 0
tot_reg_voters = 0
tot_low_reg = 0
tot_high_reg = 0


# LOOPS - Produces Outfile, % of accumulating years, counting years and ballots

while years != '':
    year = int(years)

    elgi_voters = int(eligible_voters)

    reg_voters = int(registered_voters)

    ballots = int(ballots_cast)

    per_reg = (reg_voters / elgi_voters) * 100

    per_vote = (ballots / elgi_voters) * 100

    outfile.write('In ' + str(year) + ', ' + format(per_reg, '.2f') + \
                  '% registered and  ' + format(per_vote, '.2f') + '% voted.\n')

    tot_years += 1

    tot_ballots += ballots

    tot_reg_voters += per_reg

# Total percentage of registered voters

    per_cast = (ballots / reg_voters) * 100
    
# Count how many years the % of cast is less than 60%

    if per_cast < 60:
        tot_low_reg += 1
        
# Accumlate the years thats greater than 80%

    if per_cast > 80:
        tot_high_reg += 1

# LOOP- UPDATE
    years = users_file.readline()
    eligible_voters = users_file.readline()
    registered_voters = users_file.readline()
    ballots_cast = users_file.readline()

# Calculates Average % of registered voters & % of years w/ more than 80% ballots casted


average_per_reg = tot_reg_voters / tot_years
percent_high = (tot_high_reg / tot_years) * 100

# OUTPUT
print('The total number of years listed: ' + str(tot_years) + '\n')
print('Total ballots casted in all these years: ' + format(tot_ballots, ',.0f') + '\n')
print('Average percentage of eligible voters registered: ' + format(average_per_reg, '.2f') +'%\n')
print('Number of years with less than 60% of registered voters casting ballots: ' + str(tot_low_reg) + '\n')
print('Percentage of years with more than 80% of registered voters casting ballots: ' + format(percent_high, '.1f') + '%\n' )
print('An output file named ' + outfilename + ' has been created.')
    

# Close

outfile.close()
users_file.close()
