from collections import deque


def main():
    # read the input
    materials = deque([int(x) for x in input().split()])
    magic = deque([int(x) for x in input().split()])

    # create the dataset

    materials_needed = {
        "Doll": 150,
        "Wooden train": 250,
        "Teddy bear": 300,
        "Bicycle": 400,
    }

    crafted_presents = {
        "Doll": 0,
        "Wooden train": 0,
        "Teddy bear": 0,
        "Bicycle": 0,
    }
    # mix the last material and the first magic

    while magic and materials:
        # peek the numbers
        current_material = int(materials[-1])
        current_magic = int(magic[0])
        # check if any current item is 0
        if current_magic == 0 and current_material == 0:
            magic.popleft()
            materials.pop()
            continue
        if current_material == 0:
            materials.pop()
            continue
        if current_magic == 0:
            magic.popleft()
            continue
        product = current_magic * current_material
        # check if product negative - is so, add both values and store them in materials. WHERE???
        if product < 0:
            product = current_magic + current_material
            magic.popleft()
            materials.pop()
            materials.append(product)
            continue
        # check if number positive and different then any of the values in the dataset
        if product > 0:
            if product not in materials_needed.values():
                materials[-1] += 15
                magic.popleft()
            else:
                # this would mean that the number is sufficient to craft a present
                for key, value in materials_needed.items():
                    if value == product:
                        crafted_presents[key] += 1
                        materials.pop()
                        magic.popleft()
    # print the output
    if (crafted_presents['Doll'] >= 1 and crafted_presents["Wooden train"] >= 1) or (
            crafted_presents["Teddy bear"] >= 1 and crafted_presents["Bicycle"] >= 1):
        print("The presents are crafted! Merry Christmas!")
    else:
        print("No presents this Christmas!")
    # we have to reverse the output for those two:
    magic = list(magic)
    materials = list(materials)
    if materials:
        print(f"Materials left: {', '.join([str(x) for x in materials[::-1]])}")
    if magic:
        print(f"Magic left: {', '.join([str(x) for x in magic[::-1]])}")

    sorted_items = sorted(crafted_presents.items(), key=lambda kvp: kvp[0])
    for key, value in sorted_items:
        if value > 0:
            print(f"{key}: {value}")


if __name__ == '__main__':
    main()
