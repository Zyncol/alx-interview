#!/usr/bin/python3
"""
Maria and Ben are playing a game
"""


def isWinner(x, nums):
    """x - rounds
    nums - numbers list
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    be = 0
    ma = 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for k in range(2, len(a)):
        rm_multiples(a, k)

    for k in nums:
        if sum(a[0:k + 1]) % 2 == 0:
            be += 1
        else:
            ma += 1
    if be > ma:
        return "Ben"
    if ma > be:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """removes multiple
    of prime nums
    """
    for k in range(2, len(ls)):
        try:
            ls[k * x] = 0
        except (ValueError, IndexError):
            break
