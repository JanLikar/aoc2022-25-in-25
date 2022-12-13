import ast
import functools
import itertools
import math


def cmp_int(a, b):
    return (a > b) - (a < b)


def cmp(left, right):
    match left, right:
        case (int(left), int(right)):
            return cmp_int(left, right)

        case (int(left), _):
            left = [left]

        case (_, int(right)):
            right = [right]

    for l, r in itertools.zip_longest(left, right):
        if l is None:
            return -1
        elif r is None:
            return 1

        c = cmp(l, r)

        if c != 0:
            return c
    return 0 

def parse_lines(lines):
    for line in lines:
        if len(line) == 0:
            continue

        yield ast.literal_eval(line)

lines = list(parse_lines(l.strip() for l in open("input.txt").readlines()))

pairs = zip(lines[::2], lines[1::2])
print(sum(index for index, packet in enumerate(pairs, start=1) if cmp(packet[0], packet[1]) < 0))

dividers = [[[2]], [[6]]]
lines.extend(dividers)

sorted_packets = sorted(lines, key=functools.cmp_to_key(cmp))
print(math.prod(i for i, e in enumerate(sorted_packets, start=1) if e in dividers))
