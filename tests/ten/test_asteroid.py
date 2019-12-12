import unittest
from ten.asteroid import create_map, sort_by_distance, distance, Position, blocked_positions, num_visible

class OrbitTest(unittest.TestCase):

    def test_create_map(self):
        f = open('ten/data_short.txt')

        asteroids = create_map(f)
        self.assertEqual(asteroids[0].x , 1)
        self.assertEqual(asteroids[0].y , 0)

        self.assertEqual(asteroids[1].x, 4)
        self.assertEqual(asteroids[1].y, 0)
        self.assertEqual(len(asteroids), 10)

    def test_blocked_positions_zero_distance(self):
        b_pos = blocked_positions(Position(0, 0), Position(0, 1))
        self.assertEqual(b_pos, [])

    def test_blocked_positions_same_positions(self):
        b_pos = blocked_positions(Position(0, 0), Position(0, 1))
        self.assertEqual(b_pos, [])

    def test_blocked_positions_in_same_x(self):
        b_pos = blocked_positions(Position(2, 4), Position(2, 0))
        self.assertTrue(Position(2, 3) in b_pos)
        self.assertTrue(Position(2, 2) in b_pos)
        self.assertTrue(Position(2, 1) in b_pos)

    def test_blocked_positions_in_same_y(self):
        b_pos = blocked_positions(Position(4, 2), Position(0, 2))
        self.assertTrue(Position(3, 2) in b_pos)
        self.assertTrue(Position(2, 2) in b_pos)
        self.assertTrue(Position(1, 2) in b_pos)

    def test_blocked_positions_in_same_10_4(self):
        b_pos = blocked_positions(Position(0, 0), Position(10, 4))
        self.assertTrue(Position(5, 2) in b_pos)

    def test_blocked_positions_in_same_3_3(self):
        b_pos = blocked_positions(Position(0, 0), Position(3, 3))
        self.assertTrue(Position(1, 1) in b_pos)
        self.assertTrue(Position(2, 2) in b_pos)

    def test_blocked_positions_3_4(self):
        b_pos = blocked_positions(Position(0, 0), Position(9, 12))
        self.assertTrue(Position(3, 4) in b_pos)
        self.assertTrue(Position(6, 8) in b_pos)

    def test_num_visible(self):
        f = open('ten/data_short.txt')
        asteroids = create_map(f)

        v = { s: num_visible(s, a, asteroids) for s in asteroids for a in asteroids }
        print(v)
        (max_position, count) = max(v.items(), key=lambda (k, v): v)
        (min_position, count) = min(v.items(), key=lambda (k, v): v)
        self.assertEqual(max_position.x, 3)
        self.assertEqual(max_position.y, 4)
        self.assertEqual(min_position.x, 4)
        self.assertEqual(min_position.y, 2)
