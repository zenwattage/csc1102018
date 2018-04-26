
#Scott Hansford
#CSC110
#section 05
#4/23/18
#Graphic Scene program

import Gui3

# Named Constants 
CANVAS_WIDTH = 640
CANVAS_HEIGHT = 480

# Function Definition Section -- add your function definitions here
def main():
    # draw things on the canvas

    #background circle
    canvas.circle([0,0], 200, outline='orange', width = 5, fill = 'skyblue1')
    #sun
    canvas.circle([0,100], 30, fill='gold2', outline='darkorange1', width = 3)
    
    

##    canvas.rectangle([[0,0],[50, 50]], fill='green', outline='red')
    
    canvas.polygon([[-130, -50], [-15, -50], [-70, 30]], fill = 'burlywood3', outline='burlywood4', width=2)
    canvas.polygon([[130, -50], [15, -50], [70, 30]], fill = 'burlywood3', outline='burlywood4', width=2)
    
    canvas.polygon([[-30, -50], [15, -50], [-10,3]], fill = 'cornflowerblue', outline='blue', width=2)
    
    canvas.polygon([[-70, -50], [-10, -50], [-35, 20]], fill = 'lightgreen', outline='blue', width=2)

    #ground
    canvas.line([[135, -60], [-130, -60]], width=20, fill = 'darkolivegreen4')

    #Sunburst
def sunburst_lines():
    canvas.line([[30,70],[80,40]], width = 6, fill = 'goldenrod1')
    canvas.line([[-30,70],[-80,40]], width = 6, fill = 'goldenrod1')
    canvas.line([[-50,100],[-80,100]], width = 6, fill = 'goldenrod1')
    canvas.line([[50,100],[80,100]], width = 6, fill = 'goldenrod1')
    canvas.line([[0,140],[0,180]], width = 6, fill = 'goldenrod3')
    canvas.line([[0,15],[0,60]], width = 6, fill = 'goldenrod3')
    canvas.line([[30,135],[50,160]], width = 6, fill = 'goldenrod1')
    canvas.line([[-30,135],[-50,160]], width = 6, fill = 'goldenrod1')
    



    
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
sunburst_lines()
# Here are some colors you can use: 'white', 'gray', 'black', 'red',
# 'green', 'blue', 'cyan', 'yellow', 'magenta', 'brown', 'darkgreen'
# Hundreds of colors here: http://tmml.sourceforge.net/doc/tk/colors.html

