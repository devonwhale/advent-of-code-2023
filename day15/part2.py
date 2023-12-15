import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().split(',')#.splitlines()

boxes = {}

for i in range(0, 256):
    boxes[i] = []

parsed_input = []

for section in input:
    current_value = 0
    string = ''
    special_char = ''
    focal_length = 0
    for char in section:
        if char == "\n":
            continue
        if char in ['=', '-']:
            special_char = char
            if special_char == '=':
                focal_length = int(section[-1])
            break
        ascii_value = ord(char)
        current_value += ascii_value
        current_value *= 17
        current_value = current_value % 256
        string += char
    parsed_input.append((string, current_value, special_char, focal_length))

for operation in parsed_input:
    label = operation[0]
    box = operation[1]
    symbol = operation[2]
    focal_length = operation[3]

    if symbol == '-':
        lenses_to_remove = []
        for lens in boxes[box]:
            if label in lens:
                lenses_to_remove.append(boxes[box].index(lens))
        for lens in lenses_to_remove:
            boxes[box].pop(lens)
    else:
        current_lens_index = -1
        for lens in boxes[box]:
            if label in lens:
                current_lens_index = boxes[box].index(lens)
                break
        if current_lens_index != -1:
            boxes[box][current_lens_index] = (label, focal_length)
        else:
            boxes[box].append((label, focal_length))

output = 0

for box_id, box in boxes.items():
    idx = 1
    for lens in box:
        output += (box_id + 1) * idx * lens[1]
        idx += 1

print(output)