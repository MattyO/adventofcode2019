from copy import copy

def draw(chars, points=[(0,0)]):
    if len(chars) == 0:
        return points

    next_char= chars.pop(0)
    d = next_char[0]
    num = int(next_char[1:])
    index = {'U': 1, 'D': 1, 'R': 0, 'L': 0}[d]
    muli = {'U': 1, 'D': -1, 'R': 1, 'L': -1}[d]

    new_points = []
    for i in range(1, num+1):
        new_point = list(copy(points[-1]))
        new_point[index] += muli * i
        new_point = tuple(new_point)
        new_points.append(new_point)


    return draw(chars, points + new_points)

    next(iter(chars))
    return []

def intersections(one, two):
    return set(draw(copy(one))) & set(draw(copy(two)))

def distance(one, two):
    inters = intersections(one, two)
    return min(set([abs(x) + abs(y) for x, y in inters]) - set([0]))


def wire_distance(one, two):
    inters = intersections(one, two)
    points_one = draw(one)
    points_two = draw(two)
    sums = {}

    for inter in inters:
        sums[points_one.index(inter) + points_two.index(inter)] = inter

    if 0 in sums:
        del sums[0]

    min_dist = min(sums.keys())


    return min_dist



