#!/usr/bin/python3

import sys


def theMessege(dic, total_size):
    """
    reads line by line
    compute metrics
    """

    print("File size: {}".format(total_size))
    for ky, v in sorted(dic.items()):
        if v != 0:
            print("{}: {}".format(ky, v))


total_size = 0
cd = 0
co = 0
dic = {"200": 0,
       "301": 0,
       "400": 0,
       "401": 0,
       "403": 0,
       "404": 0,
       "405": 0,
       "500": 0}

try:
    for line in sys.stdin:
        parselin = line.split()  # trimms
        parselin = parselin[::-1]  # inverts

        if len(parselin) > 2:
            co += 1

            if co <= 10:
                total_size += int(parselin[0])  # the size of the file
                cd = parselin[1]  # code status

                if (cd in dic.keys()):
                    dic[cd] += 1

            if (co == 10):
                theMessege(dic, total_size)
                co = 0

finally:
    theMessege(dic, total_size)
