import unittest
from ten.asteroid import create_map, sort_by_distance, distance, Position,  num_visible, Vector, vaporised

class OrbitTest(unittest.TestCase):

    def test_create_map(self):
        f = open('ten/data_short.txt')

        asteroids = create_map(f)
        self.assertEqual(asteroids[0].x , 1)
        self.assertEqual(asteroids[0].y , 0)

        self.assertEqual(asteroids[1].x, 4)
        self.assertEqual(asteroids[1].y, 0)
        self.assertEqual(len(asteroids), 10)

    def test_vector(self):
        computed_vector = Vector.compute(Position(0,0), Position(2,3))
        self.assertTrue(computed_vector == Vector(-3,2))

    def test_vector_is_reduced(self):
        computed_vector = Vector.compute(Position(0,0), Position(2,2))
        self.assertTrue(computed_vector == Vector(-1,1))

    def test_vector_no_x_change(self):
        computed_vector = Vector.compute(Position(0,0), Position(0,2))
        self.assertTrue(Vector.compute(Position(0,0), Position(0,2)) == Vector(-1, 0))

    def test_vector_no_y_change(self):
        computed_vector = Vector.compute(Position(0,0), Position(2,0))
        self.assertTrue(Vector.compute(Position(0,0), Position(2,0)) == Vector(0, 1))

    def test_vector_more_complex_path(self):
        computed_vector = Vector.compute(Position(1,1), Position(4,3))
        self.assertTrue(Vector.compute(Position(1,1), Position(4,3)) == Vector(-2, 3))

    def test_vector_broken(self):
        computed_vector = Vector.compute(Position(3,4), Position(2,2))
        computed_vector_2 = Vector.compute(Position(3,4), Position(1,0))
        self.assertTrue(computed_vector != computed_vector_2 )

    def test_vector_broken_2(self):
        computed_vector = Vector.compute(Position(0,1), Position(1,5))
        computed_vector_2 = Vector.compute(Position(0,1), Position(3,8))
        self.assertTrue(computed_vector != computed_vector_2 )


    def test_num_visible(self):
        f = open('ten/data_short.txt')
        asteroids = create_map(f)

        v = { s: num_visible(s, asteroids) for s in asteroids }
        (max_position, count) = max(v.items(), key=lambda (k, v): v)
        (min_position, count) = min(v.items(), key=lambda (k, v): v)
        self.assertEqual(max_position.x, 3)
        self.assertEqual(max_position.y, 4)
        self.assertEqual(min_position.x, 4)
        self.assertEqual(min_position.y, 2)


    def test_num_visible_2(self):
        f = open('ten/data_2.txt')
        asteroids = create_map(f)

        v = { s: num_visible(s, asteroids) for s in asteroids }
        (max_position, count) = max(v.items(), key=lambda (k, v): v)
        self.assertEqual(max_position, Position(5,8))
        self.assertEquals(count, 33)

    def test_num_visible_3(self):
        f = open('ten/data_3.txt')
        asteroids = create_map(f)

        v = { s: num_visible(s, asteroids) for s in asteroids}
        (max_position, count) = max(v.items(), key=lambda (k, v): v)
        self.assertEqual(max_position, Position(1,2))
        self.assertEquals(count, 35)

    def test_num_visible_4(self):
        f = open('ten/data_4.txt')
        asteroids = create_map(f)

        v = { s: num_visible(s, asteroids) for s in asteroids }
        (max_position, count) = max(v.items(), key=lambda (k, v): v)
        self.assertEqual(max_position, Position(6,3))
        self.assertEquals(count, 41)

    def test_num_visible_large(self):
        f = open('ten/data_large.txt')
        asteroids = create_map(f)

        v = { s: num_visible(s, asteroids) for s in asteroids }
        (max_position, count) = max(v.items(), key=lambda (k, v): v)
        self.assertEqual(max_position, Position(11,13))
        self.assertEquals(count, 210)

    def test_num_visible_puzzle(self):
        f = open('ten/data_puzzle.txt')
        asteroids = create_map(f)
        f.close()

        v = { s: num_visible(s, asteroids) for s in asteroids }
        (max_position, count) = max(v.items(), key=lambda (k, v): v)
        self.assertEqual(max_position, Position(13,17))
        self.assertEquals(count, 269)

    def test_vector_to_degrees(self):
        self.assertEqual(Vector(1,0).degrees(),   float(0))
        self.assertEqual(Vector(1,1).degrees(),   float(45))
        self.assertEqual(Vector(0,1).degrees(),   float(90))
        self.assertEqual(Vector(-1,1).degrees(),  float(135))
        self.assertEqual(Vector(-1,0).degrees(),  float(180))
        self.assertEqual(Vector(-1,-1).degrees(), float(225))
        self.assertEqual(Vector(0,-1).degrees(),  float(270))
        self.assertEqual(Vector(1,-1).degrees(),  float(315))

    def test_vaporized(self):
        f = open('ten/data_large.txt')
        asteroids = create_map(f)
        v = vaporised(Position(11,13),asteroids)
        self.assertEqual(v[0], Position(11,12))
        self.assertEqual(v[49], Position(16,9))
        self.assertEqual(v[198], Position(9, 6))
        self.assertEqual(v[199], Position(8,2))

    def test_vaporized_puzzle(self):
        f = open('ten/data_puzzle.txt')
        asteroids = create_map(f)
        v = vaporised(Position(13,17),asteroids)
        self.assertEqual(v[199], Position(6,12))
        self.assertEqual((v[199].x*100)+ v[199].y, 612)
