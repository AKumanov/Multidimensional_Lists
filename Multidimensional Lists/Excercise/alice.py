def get_alice_position(dirs, r, c):
    if dirs == "up":
        return r - 1, c
    elif dirs == "down":
        return r + 1, c
    elif dirs == "left":
        return r, c - 1
    return r, c + 1


def in_range(r, c, size):
    return 0 <= r < size and 0 <= c < size


#  read the matrix and find Alice's location
size = int(input())
matrix = []
alice_row, alice_col = 0, 0
for i in range(size):
    matrix.append([x for x in input().split()])
    for j in range(size):
        if matrix[i][j] == "A":
            alice_row, alice_col = i, j

tea_bags_collected = 0
while True:
    direction = input()
    alice_new_rol, alice_new_col = get_alice_position(direction, alice_row, alice_col)
    if not in_range(alice_new_rol, alice_new_col, size):
        print("Alice didn't make it to the tea party.")
        break
    if matrix[alice_new_rol][alice_new_col] == "R":
        matrix[alice_new_rol][alice_new_col] = "*"
        print("Alice didn't make it to the tea party.")
        break
    if not matrix[alice_new_rol][alice_new_col] == "." and not matrix[alice_new_rol][alice_new_col] == "*":
        tea_bags_collected += int(matrix[alice_new_rol][alice_new_col])
        matrix[alice_new_rol][alice_new_col] = "A"
        matrix[alice_row][alice_col] = "*"
        alice_row, alice_col = alice_new_rol, alice_new_col
    else:
        matrix[alice_new_rol][alice_new_col] = "A"
        matrix[alice_row][alice_col] = "*"
        alice_row, alice_col = alice_new_rol, alice_new_col

    if tea_bags_collected > 10:
        print("She did it! She went to the party.")
        break


for i in range(size):
    for j in range(size):
        if matrix[i][j] == "A":
            matrix[i][j] = "*"

for row in range(size):
    print(f"{' '.join([x for x in matrix[row]])}")
