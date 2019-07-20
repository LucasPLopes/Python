from random import randint

class Thief:#obj = Thief()
    sneaky = True
    
    def pickPocket(self):#Thief.pickpocket(gatuno) tb
        print("Called by {}".format(self))
        if(sneaky):
            return bool(randint(0,1))
        return False



            