import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_product_flammability(self):
        """Test default product flammability being 0.5."""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)

    def test_stealability(self):
        prod = Product('Test Product', price=200, weight=20)
        self.assertEqual(prod.stealability(), "Very stealable!")
    
    def test_explode(self):
        prod = Product('Test Product', flammability=2, weight=20)
        self.assertEqual(prod.explode(), '...boom!')
 


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        '''
        checks that it really does receive a list of length 30
        '''
        names = generate_products()
        self.assertEqual(len(names), 30)

    def test_legal_names(self):
        '''
        checks that the generated names for a default batch of products
         are all valid possible names to generate 
         (adjective, space, noun, from the lists of possible words)
         [assertIn(a, b) --- a in b]
        '''
        # Splits at space :text.split() Will test the presence of space between words
        
        names = generate_products() 

        for product in names:
            name = product.name
            words = name.split(' ')

            self.assertIn(words[0], ADJECTIVES)
            self.assertIn(words[1], NOUNS)
        

if __name__ == '__main__':
    unittest.main()