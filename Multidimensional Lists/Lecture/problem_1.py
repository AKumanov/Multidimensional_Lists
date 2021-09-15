data = input().split(", ")
rows = int(data[0])
cols = int(data[1])

matrix = []
total = 0
for i in range(rows):
    information = input().split(', ')
    matrix.append([])
    for j in range(cols):
        matrix[i].append(int(information[j]))

    total += sum(matrix[i])
print(total)
print(matrix)

