import unittest
from six.orbit import total_orbits, create_orbit_collection, orbit_count, Orbit, find_orbit

class OrbitTest(unittest.TestCase):
    def setUp(self):
        self.input = [
            'COM)B',
            'B)C',
            'C)D',
            'D)E',
            'E)F',
            'B)G',
            'G)H',
            'D)I',
            'E)J',
            'J)K',
            'K)L']
        self.orbit_collection = create_orbit_collection(self.input)

    def test_find_orbit(self):
        b = Orbit("B", None)
        d = Orbit('D', None) 
        test_collection = [ b, d]
        self.assertEqual(find_orbit(test_collection, 'B'), b)
        self.assertEqual(find_orbit(test_collection, 'D'), d)
        self.assertEqual(find_orbit(test_collection, 'C', default='test'), 'test')

    def test_create_orbit_collection(self):
        com = find_orbit(self.orbit_collection, "COM")
        b = find_orbit(self.orbit_collection, "B")
        c = find_orbit(self.orbit_collection, "C")
        g  = find_orbit(self.orbit_collection, "G")
        self.assertEqual(com.parent, None)
        self.assertEqual(b.parent, com)
        self.assertEqual(c.parent, b)
        self.assertEqual(g.parent, b)

    def test_orbit_count_d(self):
        self.assertEqual(orbit_count(self.orbit_collection, 'D'), 3)

    def test_orbit_count_l(self):
        self.assertEqual(orbit_count(self.orbit_collection, 'L'), 7)

    def test_orbit_count_com(self):
        self.assertEqual(orbit_count(self.orbit_collection, 'COM'), 0)

    def test_total_orbits(self):
        self.assertEqual(total_orbits(self.orbit_collection), 42)

