from collections import deque

q = deque()

nums = [x for x in input().split()]

for _ in range(len(nums)):
    q.append(nums.pop())

print(' '.join(q))
