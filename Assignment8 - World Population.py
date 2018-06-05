#Scott Hansford
#csc110
#section 5
#6/4/18
#Assignment 8  - World Population

#Program that reads data from a file and shows a report to the user.

#open and read datafile
def main():
    try:
        countries = []
        populations = []
        area = []
        averagedensity = []
        file = open('WorldData2018.txt', 'r')
        line = file.readline().rstrip()

        countries_num = sum(1 for line in open('WorldData2018.txt')) #sum of countries
        # loop through file to create each list
        for i in range(0,countries_num):
            line = line.split(',')
            country = line[0]
            pop = float(line[1])
            land = float(line[2])
            density = float(pop/land)
            countries.append(country)
            populations.append(pop)
            area.append(land)
            averagedensity.append(format(float(density), '.2f'))
            line = file.readline().rstrip()

        file.close()

        # name and pop of the country with highest pop
        # find element with max pop
        # if element has max value - store which index
        # get item with that index
        #population
        totalPopulation = sum(int(i) for i in populations)
        maxPopulation = 0
        minPopulation = 999999999
        maxArea = 0
        minArea = 999999999
        #index
        indexmaxpop = 0
        indexMinPopulation = 0
        indexMaxArea = 0
        indexMinArea = 0
        #density
        indexMaxDensity = 0
        indexMinDensity = 0
        totalDensity = (sum(float(i) for i in averagedensity)) / countries_num
        indexHighDensity = []
        indexLowDensity = []
        maxDensity = 0
        minDensity = 999999999

        for i in range(0, countries_num):
            density = float(averagedensity[i])
            if populations[i] > maxPopulation:
                maxPop = populations[i]
                indexmaxpop = i
            if area[i] > maxArea:
                maxArea = area[i]
                indexMaxArea = i
            if density > maxDensity:
                maxDensity = density
                indexMaxDensity = i
        # the name and land area of the country that has the greatest land area
        # area calculation loop
        for i in range(0, countries_num):
            density = float(averagedensity[i])
            if populations[i] < minPopulation:
                minPopulation = populations[i]
                indexMinPopulation = i
            if area[i] < minArea:
                minArea = area[i]
                indexMinArea = i
            if density < minDensity:
                minDensity = density
                indexMinDensity = i

# the name and population density of the country that has the highest population density
        #highest population loop
        for i in range(0, countries_num):
            density = float(averagedensity[i])
            highDensity = totalDensity * 2
            lowDensity = (totalDensity * (1 / 100))
            if density > highDensity:
                indexHighDensity.append(i)
            elif density <= lowDensity:
                indexLowDensity.append(i)

    # testing results
    # denselist = [0] * len(countries)
    # for i in range(len(countrylist) - 1):
    # denselist[i] = populationlist[i] / area[i]
    # print(denselist[1])

        print('*' * 50)
        print('*** This program will display World Data ***')
        print('-' * 50)
        print("The total number of countries is: {} countries".format(countries_num))
        print("The total world population is: {} people".format(totalPopulation))
        print("{} has the highest population - {} people.".format(countries[indexmaxpop], maxPop))
        print("{} has the lowest population - {} people.".format(countries[indexMinPopulation], minPopulation))
        print("{} has the greatest land area - {} sq.km".format(countries[indexMaxArea], maxArea))
        print("{} has the smallest land area - {} sq.km".format(countries[indexMinArea], minArea))
        print("{} has the highest population density - {} people/sq.km".format(countries[indexMaxDensity], maxDensity))
        print("{} has the lowest population density - {} people/sq.km".format(countries[indexMinDensity], minDensity))
        print("*"*50)
        print("Average population density is  {}".format(format(totalDensity, '.2f')))
        print("*"*50)
        print("-"*50)
        print("A list of densely populated countries (people/sq.km)")
        print("-"*50)
        for index in indexHighDensity:
            print("{}, {:>1} people/sq.km".format(countries[index], averagedensity[index]))
        print("*"*50)
        print("-"*50)
        print("A list of sparsely populated countries (people/sq.km)")
        print("-"*50)
        for index in indexLowDensity:
            print("{}, {:>1} people/sq.km".format(countries[index], averagedensity[index]))

    #exception handling
    except IOError as err:
        print(err)
    except ValueError as err:
        print(err)
main()



'''
•	the name and population density of the country that has the lowest population density
•	average population density (the average of the population densities of all the countries, not the population density of the planet as a whole)
•	a list of "densely populated countries" (those with a population density that is more than two times the average)
•	a list of "very sparsely populated countries" (those with a population density that is less than 1% of the average)
'''



'''
Example for Testing 
Total number of countries is 229
Total world population is 6950773863.000000 people
China has the highest population - 1347565324 people
Holy See has the lowest population - 459 people
Russian Federation has the greatest land area - 17075200.00 sq.km
Holy See has the smallest land area - 0.44 sq.km

Macao SAR has the highest population density - 19847.54 people/sq.km
Greenland has the lowest population density - 0.03 people/sq.km
****************************************
Average population density is 398.70
----------------------------------------
A list of densely populated countries (people/sq.km)
(those with a population density that is more than two times the average)
----------------------------------------
Bahrain		 1990.28
Bangladesh	 	 1045.09
Bermuda		 1227.87
Gibraltar	 	 4302.06
Holy See	 	 1043.18
Hong Kong SAR	 6522.15
Macao SAR	 	 19847.54
Maldives	 	 1066.94
Malta		 	 1322.33
Monaco		 17713.50
Singapore	 	 7486.19
****************************************
A list of sparsely populated countries (people/sq.km)
(those with a population density that is less than 1% of the average
----------------------------------------
Australia	 	 2.94
Botswana	 	 3.38
Canada		 3.44
Falkland Islands (Malvinas) 	 0.25
French Guiana	 2.84
Greenland	 	 0.03
Guyana		 3.52
Iceland		 3.15
Libyan Arab Jamahiriya 	 3.65
Mauritania	 	 3.44
Mongolia	 	 1.79
Namibia		 2.82
Suriname	 	 3.24
Western Sahara	 2.06

'''
