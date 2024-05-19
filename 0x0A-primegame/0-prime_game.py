#!/usr/bin/python3

""" prime numbers """


def isWinner(x, nums):
    """ prime game """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None
    
    maria = 0
    ben = 0

    y = [1 for x in range(sorted(nums)[-1] + 1)]
    y[0], y[1] = 0, 0
    for i in range(2, len(y)):
        if y[i] == 1:
            for j in range(i * i, len(y), i):
                y[j] = 0
    for i in nums:
        if sum(y[:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
return None