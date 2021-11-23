def get_next_move(dirs, r, c):
    if dirs == "up":
        return r - 1, c
    elif dirs == "down":
        return r + 1, c
    elif dirs == "left":
        return r, c - 1
    return r, c + 1


def in_range(r, c, size):
    return 0 <= r < size and 0 <= c < size


count_of_presents = int(input())
size = int(input())

happy_kids = 0
santa_row, santa_col = 0, 0
matrix = []
for i in range(size):
    matrix.append([x for x in input().split()])
    for j in range(size):
        if matrix[i][j] == "S":
            santa_row, santa_col = i, j
        if matrix[i][j] == "V":
            happy_kids += 1
have_presents = True
running = True
while running:
    if count_of_presents == 0:
        have_presents = False
        break
    direction = input()
    if direction == "Christmas morning":
        running = False
    else:
        santa_new_row, santa_new_col = get_next_move(direction, santa_row, santa_col)
        if not in_range(santa_new_row, santa_new_col, size):
            running = False
            break
        if matrix[santa_new_row][santa_new_col] == "X":
            matrix[santa_new_row][santa_new_col] = "S"
            matrix[santa_row][santa_col] = "-"
            santa_row, santa_col = santa_new_row, santa_new_col
            continue
        if matrix[santa_new_row][santa_new_col] == "V":
            count_of_presents -= 1
            matrix[santa_new_row][santa_new_col] = "S"
            matrix[santa_row][santa_col] = "-"
            santa_row, santa_col = santa_new_row, santa_new_col
            continue
        if matrix[santa_new_row][santa_new_col] == "C":
            matrix[santa_new_row][santa_new_col] = "S"
            matrix[santa_row][santa_col] = "-"
            santa_row, santa_col = santa_new_row, santa_new_col
            possible_directions = ["up", "down", "left", "right"]
            for current_direction in possible_directions:
                next_row, next_col = get_next_move(current_direction, santa_row, santa_col)
                if not in_range(next_row, next_col, size):
                    continue
                if matrix[next_row][next_col] == "V" or matrix[next_row][next_col] == "X":
                    count_of_presents -= 1
                    matrix[next_row][next_col] = "-"
                    if count_of_presents == 0:
                        have_presents = False
                        break

        else:
            matrix[santa_new_row][santa_new_col] = "S"
            matrix[santa_row][santa_col] = "-"
            santa_row, santa_col = santa_new_row, santa_new_col
        if count_of_presents == 0:
            have_presents = False
            break

if not have_presents:
    print("Santa ran out of presents!")

for i in range(size):
    print(f"{' '.join([x for x in matrix[i]])}")

good_kids_left = 0
for i in range(size):
    for j in range(size):
        if matrix[i][j] == "V":
            good_kids_left += 1

if not good_kids_left:
    print(f"Good job, Santa! {happy_kids} happy nice kid/s.")
else:
    print(f"No presents for {good_kids_left} nice kid/s.")
