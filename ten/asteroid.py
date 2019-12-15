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

class Vector():
    @classmethod
    def compute(cls, station, asteroid):

        rise = 0
        run = 0
        u_dir = 1
        y_dir = 1

        if station.x == asteroid.x or station.y == asteroid.y:
            run, rise = run_rise(station, asteroid)
            if run != 0:
                run = pos_neg(run)
            else:
                rise = pos_neg(rise)
        else:
            x_dis, y_dis = run_rise(station, asteroid)
            if x_dis != 0:
                x_dir = pos_neg(x_dis)
            if y_dis != 0:
                y_dir = pos_neg(y_dis)

            #if(station == Position(3,4)):
            #    import pdb; pdb.set_trace()

            f = fractions.Fraction(float(abs(x_dis))/abs(y_dis))
            if f.denominator > abs(x_dis):
                rise = y_dis
                run = x_dis
            else:
                rise = y_dir * f.denominator
                run = x_dir * f.numerator

        return cls(rise, run)

    def __init__(self, rise, run):
        self.rise =rise
        self.run = run

    def __eq__(self, o):
        return self.rise == o.rise and self.run == o.run

    def __repr__(self):
        return str("{}/{}".format(self.rise, self.run))

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

    if abs(x_dis) == 0:
        y_dir = pos_neg(y_dis)
        return [ Position(station.x, y) for y in range(station.y + y_dir, asteroid.y, y_dir)]
    if abs(y_dis) == 0:
        x_dir = pos_neg(x_dis)
        return [ Position(x, station.y) for x in range(station.x + x_dir, asteroid.x, x_dir)]

    x_dir = pos_neg(x_dis)
    y_dir = pos_neg(y_dis)
    f = fractions.Fraction(float(abs(x_dis))/abs(y_dis))

    if abs(f.numerator) >= abs(x_dis): return []

    x_step= f.numerator * pos_neg(x_dis)
    y_step= f.denominator* pos_neg(y_dis)


    bp = [Position(x,y) for (x, y) in zip(
                range(station.x + x_step, asteroid.x, x_step),
                range(station.y + y_step, asteroid.y, y_step))] 

    if station == Position(2,2) and asteroid == Position(4,2): import pdb; pdb.set_trace()
    return filter(lambda bp: bp != station, bp)


def num_visible(station, asteroids):
    #v = [ a for a in asteroids if not any([ p for p in blocked_positions(station, a) if p in asteroids]) and a != station]
    v = [ Vector.compute(station, a) for a in asteroids if a != station ]
    t = set( (i.rise, i.run) for i in v)
    #print(t)


    return len(t)

