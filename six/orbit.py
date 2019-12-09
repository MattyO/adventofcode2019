from collections import namedtuple

Orbit = namedtuple('Orbit', ['name', 'parent'])

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
        child_orbit = Orbit(child_name, parent_orbit)

        collection.append(child_orbit)
        if parent_orbit not in collection:
            collection.append(parent_orbit)

    return collection

def find_orbit(collection, name, default=None):
    return next((o for o in collection if o.name == name), default)

def create_orbit(collection, parent_name, leaf_name):
    return collection
