#Scott Hansford
#CSC110
#section 05
#4/23/18
#Graphic Scene program

#This isn't the scene I drew or wanted to create but I found out I was doing
#the assignment wrong and had to scramble just to meet basic requirements of the assignment

import Gui3

# Named Constants 
CANVAS_WIDTH = 640
CANVAS_HEIGHT = 480

# Function Definition Section

def background_color(color):
    canvas.config(bg = color)

def logo_ring(x,y ,radius):
    canvas.circle([x,y], radius,  fill = 'orange2', outline = 'darkorange3')
    

    
def draw_mountains(base_x, base_y, height):
    LL_x = base_x - height * 0.2
    LR_x = base_x + height * 0.2
    L_y = base_y + height * 0.5
    canvas.polygon([[base_x, base_y + height], [LL_x, L_y], [LR_x, L_y]], fill = 'darkolivegreen4')

def draw_circle(x,y, radius):
    canvas.circle([x,y],radius, fill = 'gold')

def draw_ground(base_x, base_y, height):    
    ground_x1 = base_x - height 
    ground_x2 = base_x + height 
    ground_y1 = base_y
    ground_y2 = base_y + height 
    canvas.rectangle([[ground_x1, ground_y1], [ground_x2, ground_y2]], width = 5,\
                     fill = 'lightseagreen')





def main():
    # draw things on the canvas
    background_color('darkolivegreen1')

    draw_ground(-50,-80,200)
    #background mountains
    draw_mountains(-70,70,100)
    draw_mountains(-30,70,100)
    draw_mountains(10,70,100)
    draw_mountains(50,70,100)
    draw_mountains(90,70,100)
    draw_mountains(130,70,100)    

    
    #outter circle
    logo_ring(180,50,100)
    #circles
    draw_circle(-9,59,20)
    draw_circle(4,20,20)
    draw_circle(-30,50,20)
    draw_circle(30,50,20)
    draw_circle(42,10,20)
    draw_circle(42,10,20)
    draw_circle(-35,10,20)
    draw_circle(35,10,20)






    

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
# Hundreds of colors here: https://wiki.tcl.tk/37701
# Official color documentation here:
# https://www.tcl.tk/man/tcl8.5/TkCmd/colors.htm

