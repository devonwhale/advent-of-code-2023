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

def join_check(target, destination):
    target_directions = PIPE_PIECES[target]
    for direction in target_directions:
        if CONNECTING_DIRECTIONS[direction] in PIPE_PIECES[destination]:
            return True
    return False

import os
input = open(os.path.join(os.path.dirname(__file__), "sample_input_4.txt"), 'r').read().splitlines()

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
            print(f'Found S at position {column_index}, {row_index}')
            break
    else:
        continue
    break

pipe = [[starting_column, starting_row]]
previous_direction = 'none'
pipe_complete = False

while not pipe_complete:
    #print(pipe)
    current_location = pipe[-1]
    current_row = current_location[1]
    current_column = current_location[0]
    #print(f'Current location: {current_location}')
    current_piece = map[current_row][current_column]
    #print(f'Current piece: {current_piece}')
    directions_to_assess = [direction for direction in PIPE_PIECES[current_piece].copy() if direction != previous_direction]
    for direction in directions_to_assess:
        transformation = DIRECTION_TRANSFORMATIONS[direction]
        matching_direction = CONNECTING_DIRECTIONS[direction]
        new_row = current_row + transformation[0]
        new_column = current_column + transformation[1]
        #print(new_row, max_row, new_column, max_column)
        if new_row < 0 or new_row >= max_row or new_column < 0 and new_column >= max_column:
            #print(f'Not checking location that would be out of bounds')
            continue
        new_coords = [new_column, new_row]
        symbol = map[new_row][new_column]
        if new_coords in pipe:
            #print(f'Skipping previous pipe section')
            continue
        if matching_direction not in PIPE_PIECES[symbol]:
            #print(f'Cannot match {current_piece} to a {symbol} to the {direction}')
            continue
        #print(f'Can match {current_piece} to a {symbol} to the {direction}')
        pipe.append(new_coords)
        break
    else:
        pipe_complete = True

internal_spaces = 0

for row in range(0, max_row):
    previous_symbol = '.'
    in_loop = False
    can_be_joined = False
    #print('New row')
    for column in range(0, max_column):
        current_position = [column, row]
        current_position_in_pipe = current_position in pipe
        current_symbol = map[row][column]

        #print(f'Checking {column}, {row} with symbol {current_symbol}. Current in pipe status: {current_position_in_pipe}. Current in loop status: {in_loop}')
        if current_position_in_pipe:
            if current_symbol == '-':
                #print('-, skipping')
                continue
            elif join_check(current_symbol, previous_symbol) and (previous_symbol != current_symbol):
                #print('join check failed')
                in_loop = False
            elif in_loop:
                #print('currenting in loop, exiting')
                in_loop = False
            else:
                #print('currently out of loop, entering')
                in_loop = True
        elif in_loop:
            print(f'Internal found at {column}, {row} with symbol {current_symbol}')
            internal_spaces += 1
        previous_symbol = current_symbol

print(internal_spaces)