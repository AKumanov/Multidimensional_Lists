n, m = input().split()
matrix = []

for row in range(int(n)):
    matrix.append([])
    for col in range(int(m)):
        matrix[row].append([''])

for row in range(int(n)):
    for col in range(int(m)):
        matrix[row][col] = f"{chr(ord('a') + row)}{chr(ord('a') + (row + col))}{chr(ord('a') + row)}"


for row in range(len(matrix)):
    print(' '.join(matrix[row]))
