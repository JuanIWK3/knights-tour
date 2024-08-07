import numpy as np

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


def solve_with_heuristic(board, row, col, move_counter):
    if move_counter == board.size + 1:  # Adjusted for 1-based move counter
        return True

    candidates = []
    for i in range(8):
        new_x = row + move_x[i]
        new_y = col + move_y[i]
        if validate_move(board, new_x, new_y):
            candidates.append((heuristic(board, new_x, new_y), new_x, new_y))

    candidates.sort(key=lambda x: x[0])

    for _, next_x, next_y in candidates:
        board[next_x, next_y] = move_counter
        if solve_with_heuristic(board, next_x, next_y, move_counter + 1):
            return True
        board[next_x, next_y] = 0  # Backtrack

    return False


def knights_tour(n, m, start_row, start_col):
    board = np.zeros((n, m))
    board[start_row, start_col] = 1

    if solve_with_heuristic(board, start_row, start_col, 2):
        print("Solution found")
    else:
        print("No solution exists")

    print(board)


n = 12
m = 12
start_row = 0
start_col = 0

knights_tour(n, m, start_row, start_col)
