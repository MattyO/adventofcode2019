#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from eight.picture import layers, layers_with_fewest, num_of, compute_layers
from itertools import chain, repeat
def grouper(n, iterable, padvalue=None):
            return zip(*[chain(iterable, repeat(padvalue, n-1))]*n)

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

    def test_compute_layers(self):
        new_layer = compute_layers('0222112222120000', 2, 2)
        self.assertEquals(new_layer,'0110')

    def test_part_two(self):
        f = open('eight/data.txt')
        l = f.read().strip()
        new_layer = compute_layers(l, 25,6)
        self.assertEqual(len(new_layer), 25*6)
        self.assertEqual(new_layer, "001100110011110111000110000010100101000010010100100001010010111001001010010000101111010000111001111010010100101000010100100100110010010100001001010010")
        new_layer = [ '□'  if l =='1' else '■'for l in new_layer]
        print("\n")
        for l in grouper(25, new_layer):
            print("".join(l))
        print("\n")


