import sys
from io import StringIO

test_input_1 = """3, 1, 10, 1, 2
0
"""
test_input_2 = """4, 10, 10, 6, 2, 99
2
"""

# sys.stdin = StringIO(test_input_1)
sys.stdin = StringIO(test_input_2)


jobs = [int(x) for x in input().split(', ')]
looking_for_index = int(input())
temp = []
for value, index in enumerate(jobs):
    temp.append([value, index])
temp.sort(key=lambda x: x[1])
final = 0

for index, value in temp:
    if value <= jobs[looking_for_index]:
        final += value
print(final)
