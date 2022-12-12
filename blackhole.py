# A Black_Hole is derived from a Simulton base; it updates by finding+removing
#   any objects (derived from a Prey base) whose center is crosses inside its
#   radius (and returns a set of all eaten simultons); it displays as a black
#   circle with a radius of 10 (e.g., a width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):  

    radius = 10

    def __init__(self, x, y):
        Simulton.__init__(self, x, y, 20, 20)

    def update(self, model):
        p = model.find(lambda x: isinstance(x, Prey) and self.contains(x.get_location()))
        for x in p:
            model.remove(x)
        return p


    def display(self, canvas):
        x = super().get_location()[0]
        y = super().get_location()[1]
        w = super().get_dimension()[0] / 2
        h = super().get_dimension()[1] / 2
        canvas.create_oval(x-w, y-h, x+w, y+h, fill='black')
    
    def contains(self, xy):
        return super().distance(xy) < (super().get_dimension()[0] / 2)
