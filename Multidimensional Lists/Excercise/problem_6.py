def create_matrix(i):
    board = []
    for row in range(i):
        board.append([])
        information = [x for x in input().split()]
        for col in range(len(information)):
            board[row].append(information[col])
    return board


def check_valid_input(info, row_length, col_length):
    if len(info) == 4:
        row1, col1, row2, col2 = [int(x) for x in info]
        if 0 <= row1 < row_length and 0 <= row2 < row_length and 0 <= col1 < col_length and 0 <= col2 < col_length:
            return True
    return False


def make_change(board, param):
    row1, col1, row2, col2 = [int(x) for x in param]
    board[row1][col1], board[row2][col2] = board[row2][col2], board[row1][col1]
    for i in range(len(board)):
        print(' '.join(board[i]))


n, m = [int(x) for x in input().split()]
matrix = create_matrix(n)

while True:
    data = input()
    if data == "END":
        break
    else:
        data = data.split()
        command = data[0]
        if not command == "swap":
            print('Invalid input!')
            continue
        else:
            if check_valid_input(data[1:], n, m):
                make_change(matrix, data[1:])
                continue
            else:
                print('Invalid input!')
                continue
