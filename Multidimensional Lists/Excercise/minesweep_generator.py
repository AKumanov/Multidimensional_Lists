def get_next_position(dirs, r, c):
    if dirs == "up":
        return r - 1, c
    elif dirs == "down":
        return r + 1, c
    elif dirs == "left":
        return r, c - 1
    elif dirs == "right":
        return r, c + 1
    elif dirs == "upleft":
        return r - 1, c - 1
    elif dirs == "upright":
        return r - 1, c + 1
    elif dirs == "downleft":
        return r + 1, c - 1
    elif dirs == "downright":
        return r + 1, c + 1


def in_range(r, c, size):
    return 0 <= r < size and 0 <= c < size


size = int(input())
number_of_bombs = int(input())

matrix = []
for i in range(size):
    matrix.append([x for x in (" " * size)])

for current in range(number_of_bombs):
    bomb_location = input().split()
    bomb_row = int(bomb_location[0][1])
    bomb_col = int(bomb_location[1][0])
    if not in_range(bomb_row, bomb_col, size):
        continue
    matrix[bomb_row][bomb_col] = "*"

for i in range(size):
    for j in range(size):
        if matrix[i][j] == " ":
            bombs_found = 0
            current_row, current_col = i, j
            directions = ["up", "down", "left", "right", "upleft", "upright", "downleft", "downright"]
            for direction in directions:
                new_row, new_col = get_next_position(direction, current_row, current_col)
                if not in_range(new_row, new_col, size):
                    continue
                if matrix[new_row][new_col] == "*":
                    bombs_found += 1
            matrix[i][j] = bombs_found

for row in range(size):
    print(f"{' '.join(str(x) for x in matrix[row])}")
