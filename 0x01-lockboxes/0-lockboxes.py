#!/usr/bin/python3

"""unlock boxes"""


def canUnlockAll(boxes):
    """
    check if all boxes can be unlocked
    """

    if not boxes or type(boxes) is not list:
        return False

    ubox = [0]
    for i in ubox:
        for key in boxes[i]:
            if key not in ubox and key < len(boxes):
                ubox.append(key)
    if len(ubox) == len(boxes):
        return True
    return False
