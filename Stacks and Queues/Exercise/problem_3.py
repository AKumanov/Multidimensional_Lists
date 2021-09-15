from collections import deque

qty = int(input())

q = deque()
left_over = []

data = [int(x) for x in input().split()]
# find_max
print(max(data))

for item in data:
    q.append(item)

for _ in range(len(q)):
    current = q.popleft()
    if current <= qty:
        qty -= current
    else:
        left_over.append(current)
        for _ in range(len(q)):
            left_over.append(q.popleft())
        break

if not left_over:
    print("Orders complete")
else:
    left_over = [str(x) for x in left_over]
    print(f"Orders left: {' '.join(left_over)}")
