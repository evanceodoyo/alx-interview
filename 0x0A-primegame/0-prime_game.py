#!/usr/bin/python3
"""Prime game.
"""


def isWinner(x, nums):
    """Determines the winner.
    Args:
      x (int): The number of rounds.
      nums (list): Array of n (upper limit).
    Returns:
      Name of the player that won the most rounds, otherwise None.
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)

    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= max_num:
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1

    primes = [i for i, prime in enumerate(is_prime) if prime]

    def play_game(n):
        """Game play
        """
        available = [True] * (n + 1)
        moves = 0
        for prime in primes:
            if prime > n:
                break
            if available[prime]:
                moves += 1
                for multiple in range(prime, n + 1, prime):
                    available[multiple] = False
        return moves

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        moves = play_game(n)
        if moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


print("Winner: {}".format(isWinner(3, [4, 5, 1])))
