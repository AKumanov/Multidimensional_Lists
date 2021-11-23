def in_range(r, c, field_size):
    return 0 <= r < field_size and 0 <= c < field_size


def get_next_position(dirs, r, c):
    if dirs == "up":
        return r - 1, c
    elif dirs == "down":
        return r + 1, c
    elif dirs == "left":
        return r, c - 1
    return r, c + 1


size = int(input())
snake_row, snake_col = 0, 0
matrix = []
food_collected = 0

for i in range(size):
    matrix.append([])
    information = input()
    for j in range(len(information)):
        matrix[i].append(information[j])
        if matrix[i][j] == "S":
            snake_row, snake_col = i, j

while True:
    if food_collected == 10:
        break
    direction = input()
    snake_next_row, snake_next_col = get_next_position(direction, snake_row, snake_col)
    if not in_range(snake_next_row, snake_next_col, size):
        matrix[snake_row][snake_col] = "."
        print("Game over!")
        break

    if matrix[snake_next_row][snake_next_col] == "*":
        food_collected += 1
        matrix[snake_next_row][snake_next_col] = "S"
        matrix[snake_row][snake_col] = "."
        snake_row, snake_col = snake_next_row, snake_next_col
        continue
    elif matrix[snake_next_row][snake_next_col] == "B":
        matrix[snake_next_row][snake_next_col] = "."
        matrix[snake_row][snake_col] = "."
        for i in range(size):
            for j in range(size):
                if matrix[i][j] == "B":
                    matrix[i][j] = "S"
                    snake_row, snake_col = i, j
    else:
        matrix[snake_next_row][snake_next_col] = "S"
        matrix[snake_row][snake_col] = "."
        snake_row, snake_col = snake_next_row, snake_next_col

if food_collected == 10:
    print("You won! You fed the snake.")
print(f"Food eaten: {food_collected}")
for row in range(size):
    print(f"{''.join([x for x in matrix[row]])}")
