from itertools import tee

def has_double(num):
    pw = pairwise(str(num))

    return any(map(lambda (a, b): a == b, pairwise(str(num))))

def has_only_double(num):
    pw = pairwise(str(num))
    return any([a == b and ( i ==0 or pw[i-1][0] != a) and (i == (len(pw) -1) or pw[i+1][1] != a)
        for i, (a,b) in enumerate(pw)])


def always_increases(num):
    return all(map(lambda (a, b): int(a) <= int(b), pairwise(str(num))))

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def is_valid(num):
    return len(str(num)) ==6 and has_double(num) and always_increases(num)

def is_valid2(num):
    return len(str(num)) ==6 and has_only_double(num) and always_increases(num)


