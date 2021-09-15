from collections import deque

stops = int(input())

stack = []

for i in range(stops):
    gas, distance = input().split()
    stack.append((int(gas), int(distance)))

successful_index = 0
stack = deque(stack)
current_gas = 0

success = False
while not success:
    successful_score = 0
    for index in range(len(stack)):
        gas, distance = stack[index]
        current_gas += gas
        if current_gas >= distance:
            current_gas -= distance
            successful_score += 1
        else:
            stack.append(stack.popleft())
            current_gas = 0
            successful_score = 0
            break
    if successful_score == len(stack):
        print(successful_index)
        success = True
    else:
        successful_index += 1