# Boxes.py
    
# Demonstration of Input/Processing/Output
# Calculates some characteristics of a cardboard
# box given user specifications.

# Updated to change variable naming style.

# CSC 110
# 2/2/13


# CONSTANTS -- information we already know
CARDBOARD_COST_PER_SQUARE_METER = 1.25  # in dollars per sq. meter
CARDBOARD_THICKNESS = 0.5  # centimeters
SQ_CM_PER_SQ_METER = 10000.0  # conversion factor

    
# INPUT section -- get information from the user (floating-point numbers)
message = 'Please enter the \'height\' of your box in centimeters.\nThe ' \
          +'height is the distance between the ends of the box that open: '
height = float(input(message))
message = '\nNow enter the \'length\' of your box in centimeters.\nThe ' \
          + 'length is the longer of the two remaining dimensions: '
length = float(input(message))
message = '\nFinally, enter the last dimension of your box, ' \
          + '\nits \'width\', also in centimeters: '
width = float(input(message))


# PROCESSING section -- perform calculations
    
external_volume = length * width * height;  # cubic centimeters
    
internal_volume = (length - 2 * CARDBOARD_THICKNESS) \
                  * (width - 2 * CARDBOARD_THICKNESS) \
                  * (height - 4 * CARDBOARD_THICKNESS)  # why 4?
                         
area_of_sides = (2 * length * height) + (2 * width * height)
       # 2 of each kind of "side"
       # Notice this could be reduced to:
       #   area_of_sides = 2 * (length + width) * height

area_of_flaps = (4 * length * (width / 2)) + (4 * width * (width / 2))
       # This could be reduced as well -- to what??

total_cardboard_area = area_of_sides + area_of_flaps  # area in square cm

box_cost = total_cardboard_area / SQ_CM_PER_SQ_METER \
           * CARDBOARD_COST_PER_SQUARE_METER
       # Notice this involves converting from square cm to square meters
       

# OUTPUT section -- show results
    
print('\n\nHere is your quotation:\n')
print('Box length (cm.): ' + str(length))
print('Box width (cm.): ' + str(width))
print('Box height (cm.): ' + str(height))
    
print('External volume (cubic cm.): ' + str(external_volume))
print('Internal volume (cubic cm.): ' + str(internal_volume))
print('Cardboard area (square cm.): ' + str(total_cardboard_area))
                     
print('\nYour cost per box is $' + format(box_cost, '.2f'))
print('\nThank your for visiting the \'Boxes\' page.')
print('We look forward to receiving your order!')



# Documented Test Results:

# This program was tested using the following inputs:
# height = 33
# length = 22
# width = 11

# The results produced were:
    
# Box length (cm.): 22
# Box width (cm.): 11
# Box height (cm.): 33

# External volume (cubic cm.): 7986.0
# Internal volume (cubic cm.): 6510.0
# Cardboard area (square cm.): 2904.0

# Your cost per box is $0.36
    
# These results agree with hand calculations.
    
