#!/usr/bin/python3
"""
N queens project
"""
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

t = int(sys.argv[1])


def queens(t, i=0, a=[], b=[], c=[]):
    """
    finding possible positions
    """
    if i < t:
        for p in range(t):
            if p not in a and i + p not in b and i - p not in c:
                yield from queens(t, i + 1, a + [p], b + [i + p], c + [i - p])
    else:
        yield a


def solvin(t):
    """
    solving
    """
    m = []
    i = 0
    for solution in queens(t, 0):
        for s in solution:
            m.append([i, s])
            i += 1
        print(m)
        m = []
        i = 0


solvin(t)
