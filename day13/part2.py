def calculate_score(mirror, idx_to_ignore):
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

        if valid and adjusted_index != idx_to_ignore:
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


def score(mirror, idx_to_ignore = -1):
    s = calculate_score(mirror, idx_to_ignore/100)
    if s != -1:
        return s * 100
    
    r = rotate(mirror)
    return calculate_score(r, idx_to_ignore)


import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

output = 0

unsmudged_scores = {}
idx = 0

mirror_being_built = []
for line in input:
    if line == '':
        mirror_score = score(mirror_being_built)
        unsmudged_scores[idx] = mirror_score
        idx += 1
        mirror_being_built = []
    else:
        mirror_being_built.append(line)
mirror_score = score(mirror_being_built)
unsmudged_scores[idx] = mirror_score

idx = 0
mirror_being_built = []
for line in input:
    if line == '':
        for line_idx, ml in enumerate(mirror_being_built):
            for char_idx in range(len(ml)):
                default_line = mirror_being_built[line_idx]
                if default_line[char_idx] == '.':
                    mirror_being_built[line_idx] = default_line[:char_idx] + '#' + default_line[char_idx + 1:]
                else:
                    mirror_being_built[line_idx] = default_line[:char_idx] + '.' + default_line[char_idx + 1:]
                mirror_score = score(mirror_being_built, unsmudged_scores[idx])
                if mirror_score != -1:
                    output += mirror_score
                    break
                mirror_being_built[line_idx] = default_line
            else:
                continue
            break
        idx += 1
        mirror_being_built = []
    else:
        mirror_being_built.append(line)

for line_idx, ml in enumerate(mirror_being_built):
    for char_idx in range(len(ml)):
        default_line = mirror_being_built[line_idx]
        if default_line[char_idx] == '.':
            mirror_being_built[line_idx] = default_line[:char_idx] + '#' + default_line[char_idx + 1:]
        else:
            mirror_being_built[line_idx] = default_line[:char_idx] + '.' + default_line[char_idx + 1:]
        mirror_score = score(mirror_being_built, unsmudged_scores[idx])
        if mirror_score != -1:
            output += mirror_score
            break
        mirror_being_built[line_idx] = default_line
    else:
        continue
    break

print(output)