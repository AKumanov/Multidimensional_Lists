test_input1 = """George, Hristo
17 8 21 6 13 3 24
16 D D D D D 14
7 D T T T D 15
23 D T B T D 2
9 D T T T D 22
19 D D D D D 10
12 18 4 20 5 11 1
(1, 0)
(2, 3)
(0, 0)
(4, 2)
(5, 1)
(3, 1)
(0, 0)
(2, 3)
"""

player_one, player_two = input().split(', ')

player_info = {
    player_one: [501, 1],
    player_two: [501, 1],
}


def create_matrix():
    size = 7
    board = []
    for row in range(size):
        board.append([x for x in input().split()])
    return board


turn = 1
matrix = create_matrix()


def in_range(r, c, size):
    return 0 <= r < size and 0 <= c < size


def calculate_score(board, target_row, target_col):
    x = int(board[0][target_col])
    y = int(board[-1][target_col])
    z = int(board[target_row][0])
    a = int(board[target_row][-1])
    if board[target_row][target_col] == "D":
        outcome = 2 * (x + y + z + a)
        return outcome
    if board[target_row][target_col] == "T":
        outcome = 3 * (x + y + z + a)
        return outcome
    outcome = board[target_row][target_col]
    return outcome


success = False
while True:
    information = input().split(', ')
    row = int(information[0][1])
    col = int(information[1][0])
    if not in_range(row, col, 7):
        continue
    if matrix[row][col] == "B":
        print(
            f"{player_one if turn % 2 != 0 else player_two} won the game with {player_info[player_one if turn % 2 != 0 else player_two][1]} throws!")
        break
    result = calculate_score(matrix, row, col)
    player_info[player_one if turn % 2 != 0 else player_two][0] -= int(result)
    for key, value in player_info.items():
        if value[0] <= 0:
            print(f"{key} won the game with {value[1]} throws!")
            success = True
    if success:
        break
    player_info[player_one if turn % 2 != 0 else player_two][1] += 1
    turn += 1
