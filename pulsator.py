# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole


class Pulsator(Black_Hole): 
    
    counter_constant = 30
    
    def __init__(self, x, y):
        Black_Hole.__init__(self, x, y)
        self._counter = 0
        
    def update(self, model):
        self._counter += 1
        p = super().update(model)
        for x in p:
            super().set_dimension(super().get_dimension()[0] + 1, super().get_dimension()[1] + 1)
            self._counter = 0
        if self._counter == Pulsator.counter_constant :
            super().set_dimension(super().get_dimension()[0] - 1, super().get_dimension()[1] - 1)
            self._counter = 0
            if super().get_dimension()[0] == 0 and super().get_dimension()[1] == 0:
                model.remove(self)
            
        
