#!/usr/bin/python3
"""Solves the N Queens problem"""
import sys


def n_queens(n: int):
    """
    Solves the challenge of placing N non-attacking queens on
    an N×N chessboard.

    Args:
      n (int): Number of queens
    Return:
      List of valid queen positions.

    To solve the problem, keep track of the columns that already contain
    queens in a set.
    Also keep track of the positive diagonal(bottom left to top right) [↗] and
    negative diagonal (top left to bottom right) [↘] a queen is placed in:
      - positive diagonals => row + col (is always a constant for each cell in
        a given diagonal line)
      - negative diagonals => row - col (is always a constant for each cell in
        a given diagonal line)

    For every row iteration, skip the column if it contains a queen already.
    On getting to the last row, if the queen is placed in a valid column,
    then solution is found (when row == n).
    Also skip if the given diagonal cell already exists in the
    positive/negative diagonal sets.
    """
    cols = set()
    pos_diagonals = set()
    neg_diagonals = set()
    result = []
    board = [["."] * n for _ in range(n)]

    def backtrack(row):
        """
        Implements the backtrack algorithm.
        """
        if row == n:
            row_list = []
            for r_idx, r in enumerate(board):
                for c_idx, value in enumerate(r):
                    if value == "Q":
                        row_list.append([r_idx, c_idx])

            result.append(row_list)
            return

        for col in range(n):
            pos_diag = row + col
            neg_diag = row - col
            if (
                col in cols or
                pos_diag in pos_diagonals or
                neg_diag in neg_diagonals
            ):
                continue
            cols.add(col)
            pos_diagonals.add(pos_diag)
            neg_diagonals.add(neg_diag)
            board[row][col] = "Q"
            backtrack(row + 1)

            # backtrack/clean
            cols.remove(col)
            pos_diagonals.remove(pos_diag)
            neg_diagonals.remove(neg_diag)
            board[row][col] = "."

    backtrack(0)
    return result


def main():
    """
    Driver code.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    queens = n_queens(N)
    for q in queens:
        print(q)


if __name__ == "__main__":
    main()
