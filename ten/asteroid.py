import math
import fractions
import itertools

class Position():
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return str(tuple([self.x, self.y]))
    def __eq__(self, o):
        if o == None: return False
        return self.x == o.x and self.y == o.y
    def __ne__(self, o):
        if o == None: return True
        return self.x != o.x or self.y != o.y
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

            f = fractions.Fraction(abs(y_dis), abs(x_dis))
            if f.denominator > abs(x_dis):
                rise = y_dis
                run = x_dis
            else:
                rise = y_dir * abs(f.numerator)
                run = x_dir * abs(f.denominator)

        return cls(rise, run, asteroid)

    def __init__(self, rise, run, asteroid=None):
        self.rise =rise
        self.run = run
        self.asteroid = asteroid

    def __eq__(self, o):
        return self.rise == o.rise and self.run == o.run

    def __repr__(self):
        return str("{}/{}".format(self.rise, self.run))

    def __hash__(self):
        return int(hashlib.md5('{}{}'.format(self.rise, self, run)).hexdigest(), 16)
        #return id(self)

    def degrees(self):
        d = 90 - math.atan2(self.rise, self.run) * 180 / math.pi
        if d < 0 and self.run > 0:
            d+= 180
        if d < 0 and self.run < 0:
            d+= 360
        return d

def create_map(f):
    asteroids = []
    for y, l in enumerate(f.readlines()):
        for x, c in enumerate(l):
            if c == '#':
                asteroids.append(Position(x,y))

    return asteroids

def run_rise(p1, p2):
    return (p2.x - p1.x, p1.y - p2.y )

def distance(p1, p2):
    return sum([ abs(c) for c in run_rise(p1,p2)])

def sort_by_distance(position, asteroids, funct=max):
    return sorted(asteroids, key=lambda p: distance(p, position), reverse=True)

def pos_neg(num):
    return num / abs(num)


def position_vectors(station, asteroids):
    return [ Vector.compute(station, a) for a in asteroids if a != station ]

def num_visible(station, asteroids):
    pv = position_vectors(station, asteroids)
    return len(set( (i.rise, i.run) for i in pv ))

def vaporised(station, asteroids):
    pv = position_vectors(station, asteroids)
    pv_sorted = list(sorted(pv, key=lambda v: v.degrees()))
    destroy_order = []
    vaporise_order = []

    for k, g in  itertools.groupby(pv_sorted  ):
        destroy_order.append(sorted([ v.asteroid for v in g], key=lambda p: distance(station, p)))

    max_depth = (max( len(l) for l in destroy_order))

    for d in range(0, max_depth):
        for a in destroy_order:
            vaporise_order.append(a[d] if d < len(a) else None)

    vaporise_order = [ v for v in vaporise_order if v != None]

    return vaporise_order


