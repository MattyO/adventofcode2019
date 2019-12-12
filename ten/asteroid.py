import math
import fractions

class Position():
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return str(tuple([self.x, self.y]))
    def __eq__(self, o):
        return self.x == o.x and self.y == o.y
    def __hash__(self):
        return id(self)

from collections import defaultdict
def create_map(f):
    asteroids = []
    for y, l in enumerate(f.readlines()):
        for x, c in enumerate(l):
            if c == '#':
                asteroids.append(Position(x,y))

    return asteroids

def run_rise(p1, p2):
    return (p2.x - p1.x, p2.y - p1.y )

def distance(p1, p2):
    return sum([ abs(c) for c in run_rise(p1,p2)])

def sort_by_distance(position, asteroids, funct=max):
    return sorted(asteroids, key=lambda p: distance(p, position), reverse=True)

def pos_neg(num):
    return num / abs(num)

def blocked_positions(station, asteroid):
    x_dis, y_dis = run_rise(station, asteroid)
    if distance(station, asteroid)  in  [0, 1]:
        return []
    if abs(x_dis) ==0:
        return [ Position(station.x, y) for y in range(station.y, asteroid.y, pos_neg(y_dis))]
    if abs(y_dis) ==0:
        return [ Position(x, station.y) for x in range(station.x, asteroid.x, pos_neg(x_dis))]

    f = fractions.Fraction(float(abs(x_dis))/abs(y_dis))

    if abs(f.numerator) >= abs(x_dis): return []

    bp = [Position(x,y) for (x, y) in zip(
                range(station.x, asteroid.x, f.numerator * pos_neg(x_dis)),
                range(station.y, asteroid.y, f.denominator *pos_neg(y_dis)))] 
    return list(set(bp) - set([station]))


def num_visible(station, asteroid, asteroids):
    return len([ a for a in asteroids if not any([ p for p in blocked_positions(station, a) if p in asteroids])])

