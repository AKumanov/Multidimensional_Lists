def in_range(r, c, board_length):
    return 0 <= r < board_length and 0 <= c < board_length


def get_new_position(dirs, r, c):
    if dirs == 1:
        return r - 2, c - 1
    elif dirs == 2:
        return r - 2, c + 1
    elif dirs == 3:
        return r - 1, c + 2
    elif dirs == 4:
        return r + 1, c + 2
    elif dirs == 5:
        return r + 2, c + 1
    elif dirs == 6:
        return r + 2, c - 1
    elif dirs == 7:
        return r + 1, c - 2
    elif dirs == 8:
        return r - 1, c - 2


def read_matrix(s):
    board = []
    for i in range(s):
        board.append([])
        information = input()
        for j in range(s):
            board[i].append(information[j])
    return board


def get_horse_positions(board):
    positions = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "K":
                positions.append([i, j])
    return positions


size = int(input())
matrix = read_matrix(size)
removed_horses = 0
running = True
while running:
    max_aggression = 0
    most_aggressive_horse = 0, 0
    horse_positions = get_horse_positions(matrix)
    for row, col in horse_positions:
        current_aggression = 0
        directions = [1, 2, 3, 4, 5, 6, 7, 8]
        for direction in directions:
            new_row, new_col = get_new_position(direction, row, col)
            if not in_range(new_row, new_col, size):
                continue
            if matrix[new_row][new_col] == "K":
                current_aggression += 1

        if current_aggression > max_aggression:
            max_aggression = current_aggression
            most_aggressive_horse = row, col
    if max_aggression == 0:
        running = False
    else:
        rem_row, rem_col = most_aggressive_horse
        matrix[rem_row][rem_col] = "0"
        removed_horses += 1

print(removed_horses)
