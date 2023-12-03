VALID_DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

engine = []
for line in input:
    engine.append([character for character in line])

max_char = len(engine[0])
max_line = len(engine)

line_value = 0
char_value = 0
building_number = False
valid_number = False
current_number = ''
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
                    if char_to_check not in VALID_DIGITS and not char_to_check == '.':
                        valid_number = True
        elif building_number:
            if valid_number:
                output += int(current_number)
            building_number = False
            valid_number = False
            current_number = ''
        char_value += 1
    if valid_number:
        output += int(current_number)
        building_number = False
        valid_number = False
        current_number = ''
    line_value += 1
    char_value = 0

print(output)