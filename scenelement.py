#Scott Hansford
#CSC110
#Section 05
#4/23/18
#Graphics scene


import Gui3

# Named Constants 
CANVAS_WIDTH = 640
CANVAS_HEIGHT = 480

# Function Definition Section -- add your function definitions here
def main():
    # draw things on the canvas    
    canvas.circle([-15,-15], 190, fill='grey45', outline='grey55',width = 3)
    canvas.circle([0,0], 200, fill='goldenrod1', outline='orange', width=5)
    canvas.circle([55,115], 24, fill='yellow', outline='yellow2', width=5)
    
    #polygons
    canvas.polygon([[-150, -50], [-100, 60], [-50, -50]], outline='red',fill='tomato2', width=3)
    canvas.polygon([[-30, -50], [0, 90], [50, -50]], outline='DeepSkyBlue2', fill='slateblue1',width=3)
    canvas.polygon([[150, -50], [100, 90], [50, -50]], outline='white', width=3)


    
##    canvas.rectangle([[0,0],[50, 50]], fill='green', outline='red')
   
##    canvas.line([[20, 62], [75, 42]], width=4)
##    canvas.line([[100,-105],[110,-150]], width = 6)
##    canvas.line([[-65, 40], [-55, 20], [-65, 0], [-55, -20], [-65, -40]], \
##                fill='magenta', width=2)
##    canvas.oval([[-50, -55], [50, -75]], fill='gray', width=0)
    

#####################################################################
#
# DO NOT CHANGE ANYTHING BELOW THIS LINE
#
#####################################################################

# Setup the canvas -- canvas is the drawing area
# Note that 'win' and 'canvas' are GLOBAL VARIABLES in this program
win = Gui3.Gui()
win.title('Playing around with Gui')
canvas = win.ca(width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# run the main function
main()

# show the window
win.mainloop()

# Here are some colors you can use: 'white', 'gray', 'black', 'red',
# 'green', 'blue', 'cyan', 'yellow', 'magenta', 'brown', 'darkgreen'
# Hundreds of colors here: http://tmml.sourceforge.net/doc/tk/colors.html

