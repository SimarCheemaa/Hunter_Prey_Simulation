# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


# from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey): 
        
    radius = 5 # used only for Ball; Never changes
    
    
    def __init__(self, x, y):
        Prey.__init__(self, x, y, 10, 10, None, 5)
        super().randomize_angle()
        
        
    def update(self, _):
        num = random()
        if num <= 0.3:
            speed = super().get_speed()
            if 3.5 < speed < 6.5:
                s2 = random()
                if s2 > 0.5:
                    s2 -= 1
                super().set_speed(speed + s2)
            
            angle = super().get_angle()
            a2 = random()
            if a2 > 0.5:
                a2 -= 1
            super().set_angle(angle + a2)
            
        super().move()
        

    def display(self, canvas):
        x = super().get_location()[0]
        y = super().get_location()[1]
        canvas.create_oval(x-Floater.radius, y-Floater.radius, x+Floater.radius, y+Floater.radius, fill='#FF0000')