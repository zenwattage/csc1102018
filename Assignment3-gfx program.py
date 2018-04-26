#Scott Hansford
#CSC110
#Section 05
#Graphics program - Assignment 3
#4/23/18


import Gui3

# Named Constants 
CANVAS_WIDTH = 640
CANVAS_HEIGHT = 480

# Function Definition Section -- add your function definitions here
def main():
    # draw things on the canvas
    canvas.circle([0,100], 40, fill='cornflowerblue', outline='orange')
    canvas.circle([0,0], 175, outline='orange', width = 5)

##    canvas.rectangle([[0,0],[50, 50]], fill='green', outline='red')
    canvas.polygon([[-20, -50], [10, -50], [10, 10]], fill = 'cornflowerblue', outline = 'blue', width=1)
    canvas.polygon([[-130, -50], [-10, -50], [-70, 50]], fill = 'darkorange4', outline = 'burlywood2', width=3)
    
    canvas.polygon([[-70, -50], [-10, -50], [-30, 30]], fill = 'lightgreen', outline = 'blue', width=1)
    
    canvas.line([[100, -60], [-130, -60]], width = 20, fill = 'burlywood4')
#Sunburst lines
    canvas.line([[40,25],[30,50]], width = 6, fill = 'gold')
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


