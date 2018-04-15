#Scott Hansford
#CSC110
#Section 5
#4/13/18
#Bunker Calculator
print('****'*10)
print()
#wall thickness is 1.5 meters
WALL_THICKNESS = 1.5
#density of conrete used is 2500 kg/m3
CONCRETE_DENSITY = 2500
#labor cost is 90.64 per square meter of external + internal surface area.
LABOR_COST = 90.64
#opening 1.2*1.9
OPENING = 2.28 


#prompt user for length, width, height
length = float(input("What is the length of your bunker? "))
width = float(input("What is the width of your bunker? "))
height = float(input("What is the height of your bunker? "))
print()
print('****'*10)

#calculate required outputs based on user input
##External volume (cubic m.): 336.0
external_Volume = length * width * height

##Internal volume (cubic m.): 60.0
internal_Volume = (length - 2* WALL_THICKNESS)\
                  * (width - 2 * WALL_THICKNESS) \
                  * (height - 2 * WALL_THICKNESS)

##External surface area (square m.): 289.72 ,  SA=2lw+2lh+2hw MINUS THE OPENING
external_SA = 2*(length*width) + 2*(length*height) + 2*(height*width)

##Internal surface area (square m.): 91.72
internal_SA = (2*(length*height + width*height + length*width) - WALL_THICKNESS*6) /3

##Volume of concrete (cubic m.): 272.58
vol = external_Volume - internal_Volume - WALL_THICKNESS 

##Total mass of concrete (kg): 681450.0  formula: vol*density
totalMass = CONCRETE_DENSITY * vol

##Labor cost: $34573.72
laborCost = LABOR_COST * (internal_SA + external_SA)

#output to user the required information
print("External Volume (cubic m.): ", external_Volume)
print("Internal Volume (cubic m.): ", internal_Volume)

print("External Surface Area(square m.): ", external_SA - OPENING)
print("Internal Surface Area(square m.): ", internal_SA - OPENING)

print("Volume of concrete (cubic m.): ", vol - OPENING)
print("Total mass of concrete (kg): ", totalMass)
print("Labor cost: $", laborCost)
