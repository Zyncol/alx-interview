#!/usr/bin/python3

"""
it is containing makeChange function
"""


def makeChange(coins, total):
    """
    Returns: lowest number of coins needed to meet the total
        If total is 0 or less should return 0
        If total is lower than the required coins you have return -1
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
