#!/usr/bin/env python3

"""unlock boxes"""

def canUnlockAll(boxes):
    """
    check if all boxes can be unlocked
    """

    if not boxes:
        return False

    size = len(boxes)
    x = 0
    y = {}

    for box in boxes:
        if len(box) == 0 or x == 0:
            y[x] = -1
        for key in box:
            if key < size and key != x:
                y[key] = key
        if len(y) == size:
            return True
        x += 1
    return False
