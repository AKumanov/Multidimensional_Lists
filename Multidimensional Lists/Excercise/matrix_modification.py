def read_matrix(size):
    board = []
    for _ in range(size):
        board.append([int(x) for x in input().split()])

    return board


def valid_coordinates(board, row, col):
    if 0 <= row < len(board) and 0 <= col < len(board):
        return True
    return False


def make_change(com, info, board):
    if com == "Add":
        row, col, value = [int(x) for x in info]
        if valid_coordinates(board, row, col):
            board[row][col] += value
            return board
        else:
            print("Invalid coordinates")
    elif com == "Subtract":
        row, col, value = [int(x) for x in info]
        if valid_coordinates(board, row, col):
            board[row][col] -= value
            return board
        else:
            print("Invalid coordinates")


n = int(input())

matrix = read_matrix(n)

running = True
while running:
    data = input()
    if data == "END":
        running = False
    else:
        data = data.split()
        command = data[0]
        args = data[1:]
        make_change(command, args, matrix)

for i in range(len(matrix)):
    print(' '.join([str(x) for x in matrix[i]]))
