import unittest
from read import *

# test input and file of the class READ
class TESTVALIDATE_input(unittest.TestCase):

    def setUp(self):
        with open('photos.json') as file:
            print('successful read')

    def testInput(self):
        self.assertFalse(num <1 and num >100)

