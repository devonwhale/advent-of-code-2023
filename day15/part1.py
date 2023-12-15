import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().split(',')#.splitlines()

output = 0

for section in input:
    current_value = 0
    for char in section:
        if char == "\n":
            continue
        ascii_value = ord(char)
        current_value += ascii_value
        current_value *= 17
        current_value = current_value % 256
    output += current_value

print(output)