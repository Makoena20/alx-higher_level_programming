#!/usr/bin/python3

import sys

def is_safe(board, row, col, N, result):
    for i in range(col):
        if board[i] == row or board[i] - i == row - col or board[i] + i == row + col:
            return False
    return True

def solve_nqueens(board, col, N, result):
    if col == N:
        result.append(board[:])
        return
    for i in range(N):
        if is_safe(board, i, col, N, result):
            board[col] = i
            solve_nqueens(board, col + 1, N, result)

def nqueens(N):
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [-1] * N
    result = []
    solve_nqueens(board, 0, N, result)
    for res in result:
        print([[i, res[i]] for i in range(N)])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
