#!/usr/bin/python3
"""
N-queens problem solver
"""
import sys


def print_result(result):
    """chessboard results."""
    for row in result:
        print([row.index(1), row.index(1)])


def not_in_danger(board, row, col, n):
    """Check position if safe put queen in position"""
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_with_c(board, col, n, result):
    """function to solve N-Queens using backtracking."""
    """c is a method in chess"""
    if col == n:
        result.append([row[:] for row in board])
        return

    for i in range(n):
        if not_in_danger(board, i, col, n):
            board[i][col] = 1
            solve_nqueens_with_c(board, col + 1, n, result)
            board[i][col] = 0


def solve_nqueens(n):
    """Solve n queen problem and print all results."""
    board = [[0 for _ in range(n)] for _ in range(n)]
    results = []

    solve_nqueens_with_c(board, 0, n, results)

    for result in results:
        print_result(result)


if __name__ == "__main__":
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

    solve_nqueens(N)