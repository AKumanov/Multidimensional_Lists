def read_board(n):
    matrix = []
    for i in range(n):
        matrix.append([int(x) for x in input().split(', ')])
    return matrix


def find_first_diagonal(board):
    first_diagonal = []
    for i in range(len(board)):
        for j in range(len(board)):
            if i == j:
                first_diagonal.append(board[i][j])
    return first_diagonal


def find_second_diagonal(board):
    second_diagonal = []
    for i in range(len(board) - 1, -1, -1):
        for j in range(len(board)):
            second_diagonal.append(board[i][j])
            i -= 1
            continue
        break
    return second_diagonal


def main():
    diagonals_sum = 0
    n = int(input())
    matrix = read_board(n)
    first = find_first_diagonal(matrix)
    diagonals_sum += sum(first)
    second = find_second_diagonal(matrix)
    diagonals_sum += sum(second)
    print(f"Primary diagonal: {', '.join([str(x) for x in first])}. Sum: {sum(first)}")
    print(f"Secondary diagonal: {', '.join([str(x) for x in second[::-1]])}. Sum: {sum(second)}")


if __name__ == '__main__':
    main()
