from collections import deque

# last chocolate with first cup of milk

"""
input
chocolate = [20, 24, -5, 17, 22, 60, 26]
milk = [26, 60, 22, 17, 24, 10, 55]
"""


chocolate = deque([int(x) for x in input().split(', ')])
milk = deque([int(x) for x in input().split(', ')])
milkshakes = 0

while True:
    if milkshakes == 5:
        break
    if not milk or not chocolate:
        break
    current_chocolate = chocolate.pop()
    current_milk = milk.popleft()
    if current_chocolate <= 0:
        milk.appendleft(current_milk)
        continue
    if current_milk <= 0:
        chocolate.append(current_chocolate)
        continue
    if current_milk == current_chocolate:
        milkshakes += 1
    else:
        milk.append(current_milk)
        current_chocolate -= 5
        chocolate.append(current_chocolate)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
chocolate = [str(x) for x in chocolate]
milk = [str(x) for x in milk]
if chocolate:
    print(f"Chocolate: {', '.join(chocolate)}")
else:
    print("Chocolate: empty")
if milk:
    print(f"Milk: {', '.join(milk)}")
else:
    print("Milk: empty")
