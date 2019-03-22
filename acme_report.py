from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    '''
    should generate a given number of products (default 30), randomly, and return them as a list
    '''
    products = []

    for _ in list(range(num_products)):
        product = Product(name=' '.join(sample(ADJECTIVES, k=1)+sample(NOUNS, k=1)))
        products.append(product)
    return products


def inventory_report(products):
    '''
    takes a list of products, and prints a "nice" summary
    '''

    for product in products:
        print (product.name)
        prices = []
        for price in list(range(randint(5, 100))):
            prices.append(price)
        print (sum(prices)/len(prices))

        weights = []
        for weight in list(range(randint(5,100))):
            weights.append(weight)
        print (sum(weights)/len(weights))

        flammabilities = []
        for flammability in list(range(uniform(0.0, 2.5))):
            flammabilities.append(flammability)
        print (sum(flammabilities)//len(flammabilities))

    
    
    # price = [5,100]
    # weight = [5,100]
    # flammability = (0.0, 2.5)

    # avg_price = price/len(price)
    # print('/nAverage price is:', avg_price)

    # avg_weight = weight/len(weight)
    # print('/nAverage weight is:', avg_weight)

    # avg_flam = flammability/len(flammability)
    # print('/nAverage flammability is:', avg_flam)


if __name__ == '__main__':
    inventory_report(generate_products())