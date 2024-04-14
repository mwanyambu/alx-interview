#!/usr/bin/python3
""" nqueens """
import sys

if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    sys.exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    sys.exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    sys.exit(1)

N = int(sys.argv[1])


def nQueens(N, row=0, a=[], b=[], c=[]):
    """ nQueens """
    if row < N:
        for col in range(N):
            if col not in a and row+col not in b and row-col not in c:
                yield from nQueens(N, row+1, a+[col], b+[row+col], c+[row-col])
    else:
        yield a


def solve(N):
    """ solution """
    x = []
    y = 0
    for solution in nQueens(N):
        for z in solution:
            x.append([y, z])
            y += 1
        print(x)
        x = []
        y = 0


solve(N)
