# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10). 

import random

from prey import Prey

class Ball(Prey):
    
    radius = 5 # used only for Ball; Never changes
    
    
    def __init__(self, x, y):
        super().randomize_angle()
        Prey.__init__(self, x, y, 10, 10, self.get_angle(), 15)      
        
    def update(self, _):
        super().move()

    def display(self, canvas):
        x = super().get_location()[0]
        y = super().get_location()[1]
        canvas.create_oval(x-Ball.radius, y-Ball.radius, x+Ball.radius, y+Ball.radius, fill='#0000FF')