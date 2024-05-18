#!/usr/bin/python3

""" prime numbers """


def isWinner(x, nums):
    """ prime game """
    if not nums or x < 1:
        return None
    n = max(nums)
    primes = [True for i in range(max(n + 1, 2))]
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    primes[0] = primes[1] = False
    c = 0
    for i in range(len(primes)):
        if primes[i]:
            c += 1
        primes[i] = c
    player1 = 0
    for n in nums:
        player1 += primes[n] % 2 == 0
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 < len(nums):
        return "Ben"
    return "Maria"