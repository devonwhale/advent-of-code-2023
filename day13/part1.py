def calculate_score(mirror):
    for index, row in enumerate(mirror):
        adjusted_index = index + 1
        if adjusted_index == len(mirror):
            continue
        left, right = mirror[:adjusted_index][::-1], mirror[adjusted_index:]
        shortest_list = min(len(left), len(right))

        valid = True
        for i in range(0, shortest_list):
            left_value = left[i]
            right_value = right[i]
            if left_value != right_value:
                valid = False
                break
        
        if valid:
            return adjusted_index
    return -1

def rotate(mirror):
    rotated_mirror = {}
    for char_index in range(len(mirror[0])):
        if char_index not in rotated_mirror:
            rotated_mirror[char_index] = ''
        for line in mirror:
            rotated_mirror[char_index] += line[char_index]
    return [v for v in rotated_mirror.values()]


def score(mirror):
    s = calculate_score(mirror)
    if s != -1:
        return s * 100
    
    r = rotate(mirror)
    return calculate_score(r)


import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

output = 0

mirror_being_built = []
for line in input:
    if line == '':
        output += score(mirror_being_built)
        mirror_being_built = []
    else:
        mirror_being_built.append(line)
output += score(mirror_being_built)


print(output)