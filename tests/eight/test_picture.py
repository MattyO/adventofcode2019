import unittest
import sys
import os
#sys.path.insert(0, os.getcwd())
#print(sys.path)
#import eight
#print(eight.__file__)
from eight.picture import layers, layers_with_fewest, num_of

class PictureTest(unittest.TestCase):

    def setUp(self):
        self.ls = layers('123456789012', 2,3)

    def test_layers(self):
        self.assertEqual(self.ls[0], '123456')
        self.assertEqual(self.ls[1], '789012')

    def test_layer_with_fewest(self):
        self.assertEqual(layers_with_fewest(self.ls, '3'), (1, self.ls[1]))
        self.assertEqual(layers_with_fewest(self.ls, '9'), (0, self.ls[0]))

    def test_num_of(self):
        self.assertEqual(num_of(self.ls[0], "1"), 1)
        self.assertEqual(num_of(self.ls[0], "9"), 0)

        self.assertEqual(num_of(self.ls[1], "7"), 1)
        self.assertEqual(num_of(self.ls[1], "3"), 0)

    def test_part_one(self):
        f = open('eight/data.txt')
        l = f.read().strip()

        ls = layers(l, 25,6)
        layer_num, layer = layers_with_fewest(ls, '0')
        one = num_of(layer, '1')
        two = num_of(layer, '2')
        prod = one * two 
        self.assertEqual(prod, 1806)

