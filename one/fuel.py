def calculate(mass):
    return int(mass / 3) -2

def rcalc(mass):
    extra_mass = calculate(mass)
    if extra_mass   < 0:
        return 0
    return extra_mass + rcalc(extra_mass )

def total_calc(file_name):
    return  sum([ calculate(int(line)) for line in open('data.txt') ])

def total_rcalc(file_name):
    return  sum([ rcalc(int(line)) for line in open('data.txt') ])


