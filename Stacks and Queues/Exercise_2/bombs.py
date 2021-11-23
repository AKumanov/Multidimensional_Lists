from collections import deque


# first bomb effect with the last bomb casing
def check_success(dataset):
    counter = 0
    for bomb, quantity in dataset.items():
        if quantity > 2:
            counter += 1
    if counter == 3:
        return True
    return False


# create both datasets
bomb_materials = {
    "Datura Bombs": 40,
    "Cherry Bombs": 60,
    "Smoke Decoy Bombs": 120,
}
crafted_bombs = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0,
}

#  read the input
bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings = deque([int(x) for x in input().split(', ')])

success = False
while True:
    # check if we have at least one item in both queues
    if not bomb_effects or not bomb_casings:
        break
    # check if we have enough materials to end the game
    if check_success(crafted_bombs):
        success = True
        break
    # peek
    current_bomb_effect = bomb_effects[0]
    current_bomb_casing = bomb_casings[-1]
    # check if sum of both is enough to craft a material
    found = False
    for bomb, material_needed in bomb_materials.items():
        if material_needed == (current_bomb_effect + current_bomb_casing):
            crafted_bombs[bomb] += 1
            bomb_effects.popleft()
            bomb_casings.pop()
            found = True
            break
    if not found:
        bomb_casings[-1] -= 5
        continue

# print the output
if success:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else:
    print("Bomb Effects: empty")
if bomb_casings:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings])}")
else:
    print("Bomb Casings: empty")

sorted_dict = sorted(crafted_bombs.items(), key=lambda kvp: kvp[0])

for key, value in sorted_dict:
    print(f"{key}: {value}")
