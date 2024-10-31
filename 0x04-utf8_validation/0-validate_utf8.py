#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Method that determining if given data set is representin
    a valid UTF-8 encoding.
    """
    numberOfbytes = 0

    ma_1 = 1 << 7
    ma_2 = 1 << 6

    for s in data:

        mask_byte = 1 << 7

        if numberOfbytes == 0:

            while mask_byte & s:
                numberOfbytes += 1
                mask_byte = mask_byte >> 1

            if numberOfbytes == 0:
                continue

            if numberOfbytes == 1 or numberOfbytes > 4:
                return False

        else:
            if not (s & ma_1 and not (s & ma_2)):
                return False

        numberOfbytes -= 1

    if numberOfbytes == 0:
        return True

    return False
