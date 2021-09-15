temp = input()
stack = []
score = 0
for i in range(len(temp)):
    if temp[i] == "{":
        stack.append(temp[i])
    elif temp[i] == "[":
        stack.append(temp[i])
    elif temp[i] == "(":
        stack.append(temp[i])

    if stack:
        if temp[i] == ")":
            if stack[-1] == "(":
                stack.pop()
                score += 1
        elif temp[i] == "]":
            if stack[-1] == "[":
                stack.pop()
                score += 1
        elif temp[i] == "}":
            if stack[-1] == "{":
                stack.pop()
                score += 1
    else:
        continue

if len(stack) == 0 and score > 0:
    print("YES")
else:
    print("NO")
