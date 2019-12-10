from collections import defaultdict

def layers(input_text, rows, columns):
    layers = defaultdict(list)
    for i, n in enumerate(input_text):
        layers[i / (rows*columns)].append(n)
    return { k: "".join(v) for k, v in layers.items() }

def layers_with_fewest(layers, num):

    temp_thing = [(num, k, v) for k, v in layers.items()]
    n, layer_number, layer = min(temp_thing, key= lambda (n, k,v): num_of(v,n))
    return (layer_number, layer)


def num_of(layer, num):
    return sum([ 1 for n in layer if n == num])
