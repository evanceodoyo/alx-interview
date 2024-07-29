#!/usr/bin/python3
"""
Solution for minimum coin change problem
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    dp = [(total + 1) for i in range(total + 1)]
    dp[0] = 0

    for amount in range(total + 1):
        for coin in coins:
            if amount - coin >= 0:
                dp[amount] = min(dp[amount], 1 + dp[amount - coin])

    return dp[amount] if dp[amount] != total + 1 else -1
