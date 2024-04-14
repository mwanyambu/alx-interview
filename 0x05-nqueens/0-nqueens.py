#!/usr/bin/python3
""" nqueens """
import sys

solution = []
n = 0
ind = None


def input_validation():
    """ valudate user input"""
    global n
    n = 0

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print(" must be atlearst 4")
        sys.exit(1)
    return n


def check_position(row, col):
    """ check position of queen"""
    if (row[0] == col[0] or (row[1] == col[1])):
        return True
    return abs(row[0] - col[0]) == abs(row[1] - col[1])


def check_group(group):
    """ check if group exists in solution"""
    global solution
    for s in solution:
        x = 0
        for t in s:
            for g in group:
                if t[0] == g[0] and t[1] == g[1]:
                    x += 1
        if x == n:
            return True
    return False


def get_solution(row, group):
    """ get solution for nqueens"""
    global solution
    global n

    if row == n:
        tmp = group.copy()
        if not check_group(tmp):
            solution.append(tmp)
    else:
        for col in range(n):
            a = (row * n) + col
            matches = zip(list([ind[a]]) * len(group), group)
            pos = map(lambda x: check_position(x[0], x[1]), matches)
            group.append(ind[a].copy())
            if not any(pos):
                get_solution(row + 1, group)
            group.pop(len(group) - 1)


def print_solution():
    """ print soluntion """
    global solution
    global n

    pos = list(map(lambda x: [x // n, x % n], range(n ** 2)))
    j = 0
    group = []
    get_solution(0, group)


n = input_validation()
print_solution()
for s in solution:
    print(s)
