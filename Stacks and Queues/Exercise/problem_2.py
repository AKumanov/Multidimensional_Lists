stack = []
n = int(input())

for _ in range(n):
    data = input().split()
    command = data[0]
    if command == "1":
        x = data[1]
        stack.append(x)

    elif command == "2":
        if stack:
            stack.pop()

    elif command == "3":
        if stack:
            print(max(stack))

    elif command == "4":
        if stack:
            print(min(stack))
result = []
for _ in range(len(stack)):
    result.append(stack.pop())
print(', '.join(result))

