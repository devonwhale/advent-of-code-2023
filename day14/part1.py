import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

columns = {}

line_idx = 0
for line in input:
    idx = 0
    for char in line:
        if idx not in columns:
            columns[idx] = []
        if char != '.':
            columns[idx].append((char, line_idx))
        idx += 1
    line_idx += 1

output = 0

for column, rocks in columns.items():
    previous_block = -1
    line_count = len(input) - 1
    for rock in rocks:
        if rock[0] == '#':
            previous_block = rock[1]
        elif rock[0] == 'O':
            current_position = rock[1]
            if current_position == previous_block:
                output += line_count - current_position
            else:
                output += line_count - previous_block
                previous_block += 1

print(output)


