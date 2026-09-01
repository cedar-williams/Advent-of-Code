# --- Day 4: Printing Department ---

# Count how many rolls are adjacent to the input position
def count_adj_rolls(x, y, map_list):
    adj_rolls = 0
    upper_x = len(map_list[0]) - 1
    upper_y = len(map_list) - 1

    print(f'Processing grid pos x:{x}, y:{y}')

    for x, y in (
        (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
        (x - 1, y), (x + 1, y),
        (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)
    ):

        if (x < 0) or (y < 0) or (x > upper_x) or (y > upper_y):
            continue
        else:
            if map_list[y][x] == "@":
                print(f'x: {x}, y: {y}')
                adj_rolls += 1

    print(f'{adj_rolls} rolls found')

    return adj_rolls


# Import the paper roll maps
with open("input.txt") as file:
    roll_map = [list(line.strip()) for line in file]

accessible_rolls = 0

x_pos = 0
y_pos = 0

print(f'Processing 2d array with dimensions x:{len(roll_map[0])}, y:{len(roll_map)}')

for y_index, row in enumerate(roll_map):
    for x_index, col in enumerate(row):
        if col == '@':
            adj_count = count_adj_rolls(x_index, y_index, roll_map)
            if adj_count < 4:
                accessible_rolls += 1
        print()



print(f'Accessible rolls: {accessible_rolls}')

