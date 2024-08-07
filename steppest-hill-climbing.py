import numpy as np
import random
import time

move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]


def validate_move(board, row, col):
    return (
        0 <= row < board.shape[0] and 0 <= col < board.shape[1] and board[row, col] == 0
    )


def heuristic(board, row, col):
    count = 0
    for i in range(8):
        new_x = row + move_x[i]
        new_y = col + move_y[i]
        if validate_move(board, new_x, new_y):
            count += 1
    return count


def steepest_hill_climb(board, row, col, move_counter):
    moves_made = 1
    while moves_made < 5:
        candidates = []
        for i in range(8):
            new_x = row + move_x[i]
            new_y = col + move_y[i]
            if validate_move(board, new_x, new_y):
                degree = heuristic(board, new_x, new_y)
                candidates.append((degree, new_x, new_y))

        if not candidates:
            break

        candidates.sort(key=lambda x: x[0])
        next_degree, next_x, next_y = candidates[0]

        if next_degree >= heuristic(board, row, col) and move_counter > 20:
            break

        board[next_x, next_y] = move_counter
        row, col = next_x, next_y
        move_counter += 1
        moves_made += 1

    return moves_made


def knights_tour(n, m):
    board = np.zeros((n, m))
    start_row = random.randint(0, n - 1)
    start_col = random.randint(0, m - 1)
    board[start_row, start_col] = 1

    print(f"Starting position: ({start_row}, {start_col})")

    moves_made = steepest_hill_climb(board, start_row, start_col, 2)

    print(f"Moves made: {moves_made}")
    print(board)


# Example usage
n = 16
m = 16
knights_tour(n, m)
