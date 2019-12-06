import unittest
import computer
from itertools import combinations

class ComputerTest(unittest.TestCase):
    def test_compute(self):
        i = [1, 0, 0, 0, 99 ]
        self.assertEqual(computer.compute(i), [2, 0, 0, 0, 99])

    def test_compute_2(self):
        i = [2,3,0,3,99]
        self.assertEqual(computer.compute(i), [2,3,0,6,99])

    def test_compute_3(self):
        i = [2,4,4,5,99,0]
        self.assertEqual(computer.compute(i), [2,4,4,5,99,9801])

    def test_compute_4(self):
        i = [1,1,1,4,99,5,6,0,99]
        self.assertEqual(computer.compute(i), [30,1,1,4,2,5,6,0,99])

    def setUp(self):
        f = open("data.txt").read()
        self.insruction = [int(c) for c in f.strip().split(",")]

    def test_with_replacement(self):
        self.assertEqual(computer.fix(self.insruction,12, 2)[0], 4484226)

    def test_with_replacement_handles_passing_by_referencee(self):
        self.assertEqual(computer.fix(self.insruction,12, 2)[0], 4484226)
        self.assertEqual(computer.fix(self.insruction,12, 2)[0], 4484226)


    def test_soluation(self):
        for (noun, verb) in combinations(range(0,99),2):
            if computer.fix(self.insruction, noun, verb)[0] == 19690720:
                break

        self.assertEqual(noun, 56)
        self.assertEqual(verb, 96)
        self.assertEqual(100 * noun + verb, 5696)
