from collections import deque

queue = deque()

running = True
while running:
    command = input()
    if command == "Paid":
        while queue:
            print(queue.popleft())

    elif command == "End":
        running = False

    else:
        queue.append(command)
print(f"{len(queue)} people remaining.")