from random import randint, sample, uniform
from acme import Product
import numpy

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products=30):
    '''
    should generate a given number of products (default 30), randomly, and return them as a list
    '''
    products = []

    for i in range(num_products):
        prod_name = ' '.join(sample(ADJECTIVES, k=1) + sample(NOUNS, k=1))
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform (0.0, 0.25)

        products.append(Product(prod_name, price, weight, flammability))
    return products



def inventory_report(products):
    '''
    takes a list of products, and prints a "nice" summary
    '''
    
    prices = []
    for product in products:
        prices.append(product.price)
        
    weights = []
    for weight in products:
        weights.append(product.weight)

    flammabilities = []
    for flammability in products:
        flammabilities.append(product.flammability)

    print ('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('unique_products = ', len(set(products)))
    print ('Average Price:', sum(prices)/len(prices))
    print ('Average Weight:', sum(weights)/len(weights))
    print ('Average Flammability:', sum(flammabilities)/len(flammabilities))





if __name__ == '__main__':
    inventory_report(generate_products())