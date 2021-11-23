problem = input()
stack = []

for index in range(len(problem)):
    if problem[index] == "(":
        stack.append(index)
    elif problem[index] == ")":
        start_index = stack.pop()
        print(problem[start_index: index + 1])
print(stack)
