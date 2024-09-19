#!/usr/bin/python3
"""
Given a pile of coins of different values, determine
the fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Handle edge case where total is 0 or less.
    Args:
        coins(int):  list of values of coins in possession.
        total(int):  the value of meet to find.
    Return: A integer number of possibilites found.
    """
    if total <= 0:
        return 0

    current_total = 0
    used_coins = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        r = (total - current_total) // coin
        current_total += r * coin
        used_coins += r
        if current_total == total:
            return used_coins
    return -1
