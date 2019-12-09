from collections import namedtuple

class Orbit():
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

def total_orbits(orbit_array):
    return sum( orbit_count(orbit_array, o.name) for o in orbit_array)

def orbit_count(collection, node_name):
    found_orbit = find_orbit(collection, node_name)
    if found_orbit.parent == None:
        return 0
    return 1 + orbit_count(collection, found_orbit.parent.name)

def create_orbit_collection(input_strs):
    collection = []
    for i in input_strs:
        parent_name, child_name = i.split(")")

        parent_orbit = find_orbit(collection, parent_name, Orbit(parent_name, None))
        child_orbit = find_orbit(collection, child_name, Orbit(child_name, None))
        child_orbit.parent = parent_orbit
        if child_orbit not in parent_orbit.children:
            parent_orbit.children.append(child_orbit)

        if child_orbit not in collection:
            collection.append(child_orbit)

        if parent_orbit not in collection:
            collection.append(parent_orbit)

    return collection

def find_orbit(collection, name, default=None):
    return next((o for o in collection if o.name == name), default)

def create_orbit(collection, parent_name, leaf_name):
    return collection

def parents(collection, o):
    if o.parent is None:
        return []

    return [o.parent] + parents(collection, o.parent)


def num_jumps(collection, start, end):
    start_parents_names = set([o.name for o in parents(collection, find_orbit(collection, start)) ])
    end_parents_names = set([o.name for o in parents(collection, find_orbit(collection, end)) ])

    return len(start_parents_names - end_parents_names) + len(end_parents_names - start_parents_names)
