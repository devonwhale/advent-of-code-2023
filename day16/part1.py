import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

symbol_rows = {}
symbol_columns = {}

DIRECTION_TRANSFORMATIONS = {
    'up': [-1, 0],
    'right': [0, 1],
    'down': [1, 0],
    'left': [0, -1]
}

line_idx = 0
for line in input:
    idx = 0
    symbol_rows[line_idx] = []
    for char in line:
        symbol_rows[line_idx].append((char, idx))
        if idx not in symbol_columns:
            symbol_columns[idx] = []
        symbol_columns[idx].append((char, line_idx))
        idx += 1
    line_idx += 1

heading = [('right', 0, 0)]
visited_spaces = []
unique_count = 0
loop_count = 0

for move in heading:
    #print(move)
    direction = move[0]
    row = move[1]
    column = move[2]
    visited_spaces.append((column, row))
    transformation = DIRECTION_TRANSFORMATIONS[direction]
    current_symbol = symbol_columns[column][row][0]
    #print(current_symbol)

    if current_symbol == '.':
        new_row = row + transformation[0]
        new_column = column + transformation[1]
        if new_row >= 0 and new_row < len(input) and new_column >= 0 and new_column < len(input[0]):
            heading.append((direction, new_row, new_column))
    elif current_symbol == '|':
        if direction == 'up' and row - 1 >= 0:
            heading.append((direction, row - 1, column))
        elif direction == 'down' and row + 1 < len(input):
            heading.append((direction, row + 1, column))
        else:
            if row + 1 < len(input):
                heading.append(('down', row + 1, column))
            if row - 1 >= 0:
                heading.append(('up', row - 1, column))
    elif current_symbol == '-':
        if direction == 'left' and column - 1 >= 0:
            heading.append((direction, row, column - 1))
        elif direction == 'right' and column + 1 < len(input[0]):
            heading.append((direction, row, column + 1))
        else:
            if column + 1 < len(input[0]):
                heading.append(('right', row, column + 1))
            if column - 1 >= 0:
                heading.append(('left', row, column - 1))
    elif current_symbol == '/':
        if direction == 'right' and row - 1 >= 0:
            heading.append(('up', row - 1, column))
        elif direction == 'down' and column - 1 >= 0:
            heading.append(('left', row, column - 1))
        elif direction == 'left' and row + 1 < len(input):
            heading.append(('down', row + 1, column))
        elif direction == 'up' and column + 1 < len(input[0]):
            heading.append(('right', row, column + 1))
    elif current_symbol == '\\':
        if direction == 'right' and row + 1 < len(input):
            heading.append(('down', row + 1, column))
        elif direction == 'down' and column + 1 < len(input[0]):
            heading.append(('right', row, column + 1))
        elif direction == 'left' and row - 1 >= 0:
            heading.append(('up', row - 1, column))
        elif direction == 'up' and column - 1 >= 0:
            heading.append(('left', row, column - 1))
    loop_count += 1
    if loop_count % 1000000 == 0:
        if len(set(visited_spaces)) == unique_count:
            break
        unique_count = len(set(visited_spaces))

print(len(set(visited_spaces)))