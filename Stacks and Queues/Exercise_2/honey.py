from collections import deque

# Step 1 READ INPUT
bees = deque([int(x) for x in input().split()])
nectar = deque([int(x) for x in input().split()])
symbols = deque([x for x in input().split()])

# Step 2 Implement First Part of the Process
total_honey = 0
while True:
    if bees and nectar:
        current_bee = bees.popleft()
        current_nectar = nectar.pop()
        if current_bee <= current_nectar:
            # Step 3 Implement Second Part of the Process
            current_symbol = symbols.popleft()
            total_honey += abs(eval(f"{current_bee}{current_symbol}{current_nectar}"))
        else:
            bees.appendleft(current_bee)
            continue
    else:
        break
# Output
print(f"Total honey made: {total_honey}")
if bees:
    bees = [str(x) for x in bees]
    print(f"Bees left: {', '.join(bees)}")
if nectar:
    nectar = [str(x) for x in nectar]
    print(f"Nectar left: {', '.join(nectar)}")

# possible edge cases:
"""
If there's no input:

"""