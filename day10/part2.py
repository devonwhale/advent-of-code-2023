PIPE_PIECES = {
    '|': ['north', 'south'],
    '-': ['west', 'east'],
    'L': ['north', 'east'],
    'J': ['north', 'west'],
    '7': ['south', 'west'],
    'F': ['south', 'east'],
    'S': ['north', 'east', 'south', 'west'],
    '.': []
}

CONNECTING_DIRECTIONS = {
    'north': 'south',
    'east': 'west',
    'south': 'north',
    'west': 'east'
}

DIRECTION_TRANSFORMATIONS = {
    'north': [-1, 0],
    'east': [0, 1],
    'south': [1, 0],
    'west': [0, -1]
}

import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

map = []
for line in input:
    map.append([character for character in line])

max_row = len(map)
max_column = len(map[0])

starting_row = -1
starting_column = -1

for row_index, row in enumerate(map):
    for column_index, column in enumerate(row):
        if column == 'S':
            starting_column = column_index
            starting_row = row_index
            break
    else:
        continue
    break

pipe = [[starting_column, starting_row]]
previous_direction = 'none'
pipe_complete = False

while not pipe_complete:
    current_location = pipe[-1]
    current_row = current_location[1]
    current_column = current_location[0]
    current_piece = map[current_row][current_column]
    directions_to_assess = [direction for direction in PIPE_PIECES[current_piece].copy() if direction != previous_direction]
    for direction in directions_to_assess:
        transformation = DIRECTION_TRANSFORMATIONS[direction]
        matching_direction = CONNECTING_DIRECTIONS[direction]
        new_row = current_row + transformation[0]
        new_column = current_column + transformation[1]
        if new_row < 0 or new_row >= max_row or new_column < 0 and new_column >= max_column:
            continue
        new_coords = [new_column, new_row]
        symbol = map[new_row][new_column]
        if new_coords in pipe:
            continue
        if matching_direction not in PIPE_PIECES[symbol]:
            continue
        pipe.append(new_coords)
        break
    else:
        pipe_complete = True

# https://en.wikipedia.org/wiki/Shoelace_formula
corners = [position for position in pipe if map[position[1]][position[0]] in ['F', 'J', 'L', '7', 'S']]

final_corner_index = len(corners) - 1
x_by_next_y = corners[final_corner_index][0] * corners[0][1]
y_by_next_x = corners[0][0] * corners[final_corner_index][1]
for index in range(0, final_corner_index):
    x_by_next_y += corners[index][0] * corners[index + 1][1]
    y_by_next_x += corners[index][1] * corners[index + 1][0]

internal_area = abs(x_by_next_y - y_by_next_x) / 2

# https://en.wikipedia.org/wiki/Pick%27s_theorem
print(internal_area - (len(pipe) / 2) + 1)