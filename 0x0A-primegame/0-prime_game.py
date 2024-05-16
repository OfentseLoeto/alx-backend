#!/usr/bin/python3
"""
Prime game between Maria and Ben.
"""


def isWinner(x, nums):
    """
    Determines the winner of multiple rounds of the prime game.

    Args:
        x (int): The number of rounds.
        nums (list): An array of integers representing the upper
                     bounds for each round.

    Returns:
        str or None: The name of the player that won the most rounds.
                     If the winner cannot be determined, returns None.
    """
    def is_Prime(n):
        """
        Checks if a number is prime.

        Args:
            n (int): The number to check.

        Returns:
            bool: True if n is prime, False otherwise.
        """
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def winner(n):
        count = 0
        for i in range(2, n + 1):
            if is_Prime(i):
                count += 1
        return "Ben" if count % 2 == 0 else "Maria"

    # Determine the winner of each round
    result = [winner(num) for num in nums]

    # Count the number of wins for Maria and Ben
    maria_wins = result.count("Maria")
    ben_wins = result.count("Ben")

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"

    else:
        return None
