def in_range(r, c, size):
    return 0 <= r < size and 0 <= c < size


def get_next_position(dirs, r, c, step=1):
    if dirs == "up":
        return r - step, c
    elif dirs == "down":
        return r + step, c
    elif dirs == "left":
        return r, c - step
    return r, c + step


total_targets = 0
size = 5
matrix = []
player_row, player_col = 0, 0
for i in range(size):
    matrix.append([x for x in input().split()])
    for j in range(size):
        if matrix[i][j] == "A":
            player_row, player_col = i, j
        if matrix[i][j] == "x":
            total_targets += 1

n = int(input())
targets_hit = []
for _ in range(n):
    line_args = input().split()
    command = line_args[0]
    direction = line_args[1]

    if command == "move":
        steps = int(line_args[2])
        new_player_row, new_player_col = get_next_position(direction, player_row, player_col, steps)
        if not in_range(new_player_row, new_player_col, size):
            continue
        if not matrix[new_player_row][new_player_col] == ".":
            continue
        matrix[new_player_row][new_player_col] = "A"
        matrix[player_row][player_col] = "."
        player_row, player_col = new_player_row, new_player_col

    else:

        bullet_row, bullet_col = get_next_position(direction, player_row, player_col)
        while True:
            if not in_range(bullet_row, bullet_col, size):
                break
            if matrix[bullet_row][bullet_col] == "x":
                matrix[bullet_row][bullet_col] = "."
                targets_hit.append([bullet_row, bullet_col])
                break
            bullet_row, bullet_col = get_next_position(direction, bullet_row, bullet_col)
    if total_targets == len(targets_hit):
        break

if total_targets == len(targets_hit):
    print(f"Training completed! All {total_targets} targets hit.")
else:
    print(f"Training not completed! {total_targets - len(targets_hit)} targets left.")

for target in targets_hit:
    print(target)
