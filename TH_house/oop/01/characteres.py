from random import randint

class Thief:#obj = Thief()
    sneaky = True
    
    def pickPocket(self):#Thief.pickPocket(gatuno) tb
        print("Called by {}".format(self))
        if self.sneaky:
            return bool(randint(0,1))
        return False

class Thief2(object):
    sneaky: True    #sorrateiro
    
    def pickPocket(self):
        if self.sneaky:
            return bool(randint(0,1))
        return False

    def hide(self, light_level):
        return self.sneaky and light_level <= 10 

            