class Part:
    def __init__(self, number, adjacent_gears):
        self.number = number
        self.adjacent_gears = adjacent_gears

VALID_DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

engine = []
for line in input:
    engine.append([character for character in line])

max_char = len(engine[0])
max_line = len(engine)

# Build up all possible part numbers
line_value = 0
char_value = 0
building_number = False
current_number = ''
parts = []
gear_locations = []
adjacent_gears = []
output = 0
for line in engine:
    for char in line:
        if char in VALID_DIGITS:
            building_number = True
            current_number += char

            for x_to_check in [line_value - 1, line_value, line_value + 1]:
                if x_to_check < 0 or x_to_check > max_line - 1:
                    continue
                for y_to_check in [char_value - 1, char_value, char_value + 1]:
                    if y_to_check < 0 or y_to_check > max_char - 1:
                        continue
                    char_to_check = engine[x_to_check][y_to_check]
                    if char_to_check == '*':
                        adjacent_gears.append(f'{x_to_check},{y_to_check}')
        elif building_number or char_value == max_char:
            parts.append(Part(int(current_number), set(adjacent_gears)))
            building_number = False
            current_number = ''
            adjacent_gears = []
        if char == '*':
            gear_locations.append([line_value, char_value])
        char_value += 1
    if not current_number == '':
        parts.append(Part(int(current_number), set(adjacent_gears)))
        building_number = False
        current_number = ''
        adjacent_gears = []
    line_value += 1
    char_value = 0

print(gear_locations)
for gear in gear_locations:
    adjacent_parts = []
    gear_value = f'{gear[0]},{gear[1]}'
    for part in parts:
        if gear_value in part.adjacent_gears:
            adjacent_parts.append(part.number)
    if len(adjacent_parts) == 2:
        print(f'Gear at {gear} is adjacent to {adjacent_parts[0]} and {adjacent_parts[1]}')
        gear_ratio = adjacent_parts[0] * adjacent_parts[1]
        output += gear_ratio


print(output)