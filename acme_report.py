from random import randint, sample, uniform
from acme import Product
import numpy

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
def generate_products(num_products=30):
    '''
    should generate a given number of products (default 30), randomly, and return them as a list
    '''
    products = []

    for product in list(range(num_products)):
        product = Product(name=' '.join(sample(ADJECTIVES, k=1) + sample(NOUNS, k=1)))
        products.append(product)

    
    return products


def inventory_report(products):
    '''
    takes a list of products, and prints a "nice" summary
    '''
    unique_products = set(products)
    print('unique_products = ', len(unique_products))


    for product in products:
        print ('Product Name:', product.name)
        prices = []
        for price in list(range(randint(5, 100))):
            prices.append(price)
        print ('Average Price:', sum(prices)/len(prices))

        weights = []
        for weight in list(range(randint(5,100))):
            weights.append(weight)
        print ('Average Weight:', sum(weights)/len(weights))

        flammabilities = []
        for flammability in list(numpy.arange(uniform(0.0,2.5))):
            flammabilities.append(flammability)
        print ('Average Flammability:', sum(flammabilities)/len(flammabilities))




if __name__ == '__main__':
    inventory_report(generate_products())