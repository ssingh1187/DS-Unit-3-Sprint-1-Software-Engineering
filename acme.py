import random

class Product:
    '''
    Parameters
    ----------------
    name : string with no default
    price : integer with default value 10
    weight : integer with default value 20
    flammability : float with default value 0.5
    identifier : (integer, automatically genererated as a random (uniform) number
                 anywhere from 1000000 to 9999999, inclusive).
    '''

    def __init__(self, name=None, price=10, weight=20, flammability=0.5,
                identifier=random.randint(1000000, 10000000)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier 

    def stealability(self):
        '''calculates the price divided by the weight  
        if the ratio is less than 0.5 return "Not so stealable...", 
        if it is greater or equal to 0.5 but less than 1.0 return "Kinda stealable.", 
        and otherwise return "Very stealable!"
        '''
        stealability = self.price/self.weight
        if stealability < 0.5:
            print('Not so stealable...')
        elif stealability >= 0.5 and stealability < 1.0:
            print('Kinda stealable.')
        else:
            print('Very stealable!')


        def explode(self):
            '''
            calculates the flammability times the weight, 
            and then returns a message: if the product is less than 10 return "...fizzle.", 
            if it is greater or equal to 10 but less than 50 return "...boom!", and otherwise return "...BABOOM!!"
            '''
            explode = self.flammability * self.weight
            if explode < 10:
                print('...fizzle.')
            elif explode >= 10 and Product < 50:
                print('...boom!')
            else:
                print('...BABOOM!!')
            
