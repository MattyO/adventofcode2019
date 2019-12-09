import unittest
from six.orbit import total_orbits, create_orbit_collection, orbit_count, Orbit, find_orbit, parents, num_jumps

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
        h  = find_orbit(self.orbit_collection, "H")
        self.assertEqual(com.parent, None)
        self.assertEqual(b.parent, com)
        self.assertEqual(b.children, [c,g])
        self.assertEqual(c.parent, b)
        self.assertEqual(g.parent, b)
        self.assertEqual(h.children, [])

    def test_orbit_count_d(self):
        self.assertEqual(orbit_count(self.orbit_collection, 'D'), 3)

    def test_orbit_count_l(self):
        self.assertEqual(orbit_count(self.orbit_collection, 'L'), 7)

    def test_orbit_count_com(self):
        self.assertEqual(orbit_count(self.orbit_collection, 'COM'), 0)

    def test_total_orbits(self):
        self.assertEqual(total_orbits(self.orbit_collection), 42)

    def test_child_is_added_after_parent(self):
        orbit_collection = create_orbit_collection(['B)C','COM)B'])
        self.assertEqual(len(orbit_collection), 3)
        self.assertEqual(find_orbit(orbit_collection, "B").parent.name, "COM")
        self.assertEqual(find_orbit(orbit_collection, "C").parent.name, "B")

    def test_parents(self):
        b = find_orbit(self.orbit_collection, "B")
        h = find_orbit(self.orbit_collection, "H")
        self.assertEqual([o.name for o in parents(self.orbit_collection, b)], ["COM"])
        self.assertEqual([o.name for o in parents(self.orbit_collection, h)], ["G", "B", "COM"])

    def test_min_jumps_up(self):
        test_input = self.input + [
            'K)YOU',
            'J)SAN',
        ]
        self.assertEqual(num_jumps(create_orbit_collection(test_input), "YOU", "SAN"), 1)

    def test_min_jumps_down(self):
        test_input = self.input + [
            'K)YOU',
            'F)SAN',
        ]

        self.assertEqual(num_jumps(create_orbit_collection(test_input), "YOU", "SAN"), 3)

    def test_min_jumps_up2_down_one(self):
        test_input = self.input + [
            'K)YOU',
            'I)SAN',
        ]

        self.assertEqual(num_jumps(create_orbit_collection(test_input), "YOU", "SAN"), 4)

    def test_output_pt_2(self):
        f = open('six/data.txt')
        i = [ l.strip() for l in f.readlines() ]
        c = create_orbit_collection(i)

        self.assertEqual(num_jumps(c, "YOU", "SAN"), 274)


