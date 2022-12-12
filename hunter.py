# A Hunter class is derived from a Pulsator and then Mobile_Simulton base.
#   It inherits updating+displaying from Pusator/Mobile_Simulton: it pursues
#   any close prey, or moves in a straight line (see Mobile_Simultion).


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):  
    
    def __init__(self, x, y):
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.set_speed(self, 5)
        Mobile_Simulton.randomize_angle(self)
    
    def update(self, model):
        
        p = model.find(lambda x: (isinstance(x, Prey)) and x.distance(self.get_location()) <= 200)
        if p != set():
            c = sorted(p, key=lambda x: x.distance(self.get_location()))[0]   
            cx = c.get_location()[0]
            cy = c.get_location()[1]
            x = self.get_location()[0]
            y = self.get_location()[1]
            x2 = cx - x
            y2 = cy - y
            ang = atan2(y2, x2)
            self.set_angle(ang)

        
        Pulsator.update(self, model)
        super().move()