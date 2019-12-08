import unittest

from intersection import draw, intersections, distance, wire_distnace

class IntersectionTest(unittest.TestCase):

    def test_up(self):
        self.assertEqual(draw(['U3']), [(0,0), (0,1), (0,2), (0,3)])
        self.assertEqual(draw(['U33']), zip([0]*34, range(0,34)))

    def test_down(self):
        self.assertEqual(draw(['D3']), [(0,0), (0,-1), (0,-2), (0,-3)])

    def test_right(self):
        self.assertEqual(draw(['R3']), [(0,0), (1,0), (2,0), (3,0)])

    def test_left(self):
        self.assertEqual(draw(['L3']), [(0,0), (-1,0), (-2,0), (-3,0)])

    def test_two_chars(self):
        self.assertEqual(draw(['U2', 'R2', 'L1']), [(0,0), (0,1), (0,2), (1, 2), (2,2), (1,2)])

    def test_intersection(self):
        self.assertEquals(
            intersections(['R8','U5','L5','D3'], ['U7','R6','D4','L4']),
            set([(0, 0), (3, 3), (6, 5)])
        )

    def test_min_distance(self):
        self.assertEquals(
            distance(['R8','U5','L5','D3'], ['U7','R6','D4','L4']),
            6
        )

    def test_min_distance2(self):
        self.assertEquals(
            distance(
                ['R75','D30','R83','U83','L12','D49','R71','U7','L72'], 
                ['U62','R66','U55','R34','D71','R55','D58','R83']),
            159
        )

    def test_min_distance3(self):
        self.assertEquals(
            distance(
                ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'], 
                ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']),
            135
        )

    def test_min_wire_distance(self):
        self.assertEquals(
            wire_distance(
                ['R75','D30','R83','U83','L12','D49','R71','U7','L72'], 
                ['U62','R66','U55','R34','D71','R55','D58','R83']),
            610
        )

    def test_min_wire_distance2(self):
        self.assertEquals(
            wire_distance(
                ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'], 
                ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']),
            410
        )

    def test_min_wire_distance_happy(self):
        self.assertEquals(
            wire_distance(['R8','U5','L5','D3'], ['U7','R6','D4','L4']),
            30
        )


