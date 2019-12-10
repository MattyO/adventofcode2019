from collections import defaultdict

def layers(input_text, width, height):
    layers = defaultdict(list)
    for i, n in enumerate(input_text):
        layers[i / (height*width)].append(n)
    return { k: "".join(v) for k, v in layers.items() }

def layers_with_fewest(layers, num):

    temp_thing = [(num, k, v) for k, v in layers.items()]
    n, layer_number, layer = min(temp_thing, key= lambda (n, k,v): num_of(v,n))
    return (layer_number, layer)


def num_of(layer, num):
    return sum([ 1 for n in layer if n == num])

def compute_layers(ls, width, height):
    ls = layers(ls, width, height)
    num_layers = len(ls)
    layer_size = len(ls[0])

    temp_layers=[]

    for i in range(0, layer_size):
        temp_layers.append([ls[l][i] for l in range(0, num_layers)])

    return "".join([ "".join(l).replace("2", "")[0] for l in temp_layers])





