from copy import copy
from functools import reduce
def mult(iterable):
    return reduce(lambda i,j: i * j, iterable)

operators = (sum, mult)

def compute(lines, pointer=0):
    if lines[pointer]== 99 or pointer >= len(lines):
        return lines

    command, o1, o2, end_pos = lines[pointer: pointer+4]
    new_lines = copy(lines)
    new_lines[end_pos] = operators[command-1]([lines[o1], lines[o2]])
    return compute(new_lines, pointer+4)

def fix(lines, noun, verb):
    lines[1], lines[2] = noun, verb
    return compute(lines)


