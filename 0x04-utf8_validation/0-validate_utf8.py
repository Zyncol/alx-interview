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

    m_1 = 1 << 7
    m_2 = 1 << 6

    for i in data:

        mask_byte = 1 << 7

        if numberOfbytes == 0:

            while mask_byte & i:
                numberOfbytes += 1
                mask_byte = mask_byte >> 1

            if numberOfbytes == 0:
                continue

            if numberOfbytes == 1 or numberOfbytes > 4:
                return False

        else:
            if not (i & m_1 and not (i & m_2)):
                    return False

        numberOfbytes -= 1

    if numberOfbytes == 0:
        return True

    return False
