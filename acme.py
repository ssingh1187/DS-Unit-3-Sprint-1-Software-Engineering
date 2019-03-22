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
        print(identifier)

    def stealability(self):
        '''calculates the price divided by the weight  
        if the ratio is less than 0.5 return "Not so stealable...", 
        if it is greater or equal to 0.5 but less than 1.0 return "Kinda stealable.", 
        and otherwise return "Very stealable!"
        '''
        stealability = self.price/self.weight
        if stealability < 0.5:
            return ('Not so stealable...')
        elif stealability >= 0.5 and stealability < 1.0:
            return ('Kinda stealable.')
        else:
            return ('Very stealable!') 


    def explode(self):
        '''
        calculates the flammability times the weight, 
        and then returns a message: if the product is less than 10 return "...fizzle.", 
        if it is greater or equal to 10 but less than 50 return "...boom!", and otherwise return "...BABOOM!!"
        '''
        explode = self.flammability * self.weight
        if explode < 10:
            return('...fizzle.')
        elif explode >= 10 and explode < 50:
            return('...boom!')
        else:
             return('...BABOOM!!')

        
# class BoxingGlove(Product):
#     def __init__(self, name=None, price=10, weight=10, flammability=0.5,
#                          identifier=random.randint(1000000, 10000000)):
#         super().__init__(name=name, price=price, weight=weight, flammability=flammability,identifier=identifier)

#     def explode(self):
#         explode = self.flammability * self.weight
#         if explode < 10:
#             return('...its a glove.')
#         elif explode >= 10 and Product < 50:
#             return('...its a glove.')
#         else:
#             return('...its a glove.')

#     def punch(self):
#         if self.weight < 5:
#             return('That tickles.')
#         elif self.weight >= 5 and self.weight < 15:
#             return('Hey that hurt!')
#         else:
#             return('OUCH!')
