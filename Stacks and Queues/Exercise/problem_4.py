box = [int(x) for x in input().split()]
capacity = int(input())

current_weight = 0
racks = 1

for i in range(len(box)):
    current_item = box.pop()
    if current_item + current_weight > capacity:
        racks += 1
        current_weight = 0
    current_weight += current_item

print(racks)
