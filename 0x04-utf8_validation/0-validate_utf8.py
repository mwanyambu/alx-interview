#!/usr/bin/python3

""" utf-8 validation """


def validUTF8(data):
    """
    method that determines if a given data set represents valid UTF-8 encoding
    """
    x = 0
    while x < len(data):
        bytess = 0
        mask = 0b10000000

        while mask & data[x]:
            bytess += 1
            mask >>= 1

        if bytess < 1 or bytess > 4:
            return False
        if x + bytess > len(data):
            return False

        for y in range(x + 1, x + bytess):
            if not (data[y] & 0b11000000 == 0b10000000):
                return False

        x += bytess

    return True
