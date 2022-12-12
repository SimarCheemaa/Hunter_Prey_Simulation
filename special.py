#Special is a special prey that is a random color, is shaped square and whenever in 
#proximity of a BlackHole object (Blackhole, Pulsator and Hunter) 
#It speeds up and runs away in the opposite angle

from prey import Prey
from blackhole import Black_Hole
import random
from math import atan2

class Special(Prey):
    
    radius = 10
    
    def __init__(self, x, y):
        super().randomize_angle()
        Prey.__init__(self, x , y, 20, 20, self.get_angle(), 5)
        self._color = self.random_color()
    
    @staticmethod
    def random_color():
        return "#"+str(hex(random.randint(20,255)))[2:]+str(hex(random.randint(20,255)))[2:]+str(hex(random.randint(20,255)))[2:]
        
    def update(self, model):
        p = model.find(lambda x: (isinstance(x, Black_Hole)) and x.distance(self.get_location()) <= 200)
        if p != set():
            c = sorted(p, key=lambda x: x.distance(self.get_location()))[0]
            cx = c.get_location()[0]
            cy = c.get_location()[1]
            x = self.get_location()[0]
            y = self.get_location()[1]
            x2 = cx - x
            y2 = cy - y
            ang = atan2(x2, y2)
            self.set_angle(ang)
            super().set_speed(7)
            
        super().move()

    def display(self, canvas):
        x = super().get_location()[0]
        y = super().get_location()[1]
        canvas.create_rectangle(x-Special.radius, y-Special.radius, x+Special.radius, y+Special.radius, fill=self._color)
