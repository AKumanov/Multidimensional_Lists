def read_board(n):
    board = []
    for row in range(n):
        board.append([x for x in input().split()])
    return board


def locate_bunny(board):
    for i in range(size):
        for j in range(size):
            if board[i][j] == "B":
                return i, j


def make_move(r, c, dirs):
    if dirs == "up":
        return r - 1, c
    elif dirs == "down":
        return r + 1, c
    elif dirs == "left":
        return r, c - 1
    return r, c + 1


def check_if_in_range(r, c, n):
    return 0 <= r < n and 0 <= c < n


best_direction = ""
best_path = []
max_eggs_collected = float('-inf')
possible_directions = ["up", "down", "left", "right"]

size = int(input())
matrix = read_board(size)

for direction in possible_directions:
    current_path = []
    bunny_row, bunny_col = locate_bunny(matrix)
    eggs_collected = 0
    running = True
    while running:
        next_row, next_col = make_move(bunny_row, bunny_col, direction)
        if not check_if_in_range(next_row, next_col, size):
            running = False
            break
        if matrix[next_row][next_col] == "X":
            running = False
            break
        eggs_collected += int(matrix[next_row][next_col])
        current_path.append([next_row, next_col])
        bunny_row, bunny_col = next_row, next_col
    if eggs_collected > max_eggs_collected:
        max_eggs_collected = eggs_collected
        best_direction = direction
        best_path = current_path

print(best_direction)
for i in best_path:
    print(i)
print(max_eggs_collected)
