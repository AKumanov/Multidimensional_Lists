import math


def check_range(r, c, s):
    return 0 <= r < s and 0 <= c < s


def get_next_position(dirs, r, c):
    if dirs == "up":
        return r - 1, c
    elif dirs == "down":
        return r + 1, c
    elif dirs == "left":
        return r, c - 1
    return r, c + 1


path = []
coins = 0
matrix = []
size = int(input())
player_row, player_col = 0, 0
for i in range(size):
    matrix.append([x for x in input().split()])
    for j in range(size):
        if matrix[i][j] == "P":
            player_row, player_col = i, j

success = False
while True:
    direction = input()
    new_player_row, new_player_col = get_next_position(direction, player_row, player_col)
    if not check_range(new_player_row, new_player_col, size):
        coins /= 2
        break
    if matrix[new_player_row][new_player_col] == "X":
        coins /= 2
        break
    coins += int(matrix[new_player_row][new_player_col])
    path.append([new_player_row, new_player_col])
    if coins >= 100:
        success = True
        break

    player_row, player_col = new_player_row, new_player_col
if not success:
    print(f"Game over! You've collected {math.floor(coins)} coins.")
else:
    print(f"You won! You've collected {coins} coins.")
print("Your path:")
for current in path:
    print(current)
