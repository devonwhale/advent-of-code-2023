def is_list_zeroed(list):
    for item in list:
        if item != 0:
            return False
    return True

import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

output = 0

for line in input:
    sequences = [list(map(lambda x:int(x), line.split()))]
    while not is_list_zeroed(sequences[-1]):
        differences = []
        for index, value in enumerate(sequences[-1]):
            if index == 0:
                continue
            differences.append(sequences[-1][index] - sequences[-1][index-1])
        sequences.append(differences)
    
    for index in range(len(sequences) - 1, 0, -1):
        current_line = sequences[index]
        difference_for_next_line = current_line[-1]
        sequences[index - 1].append(sequences[index - 1][-1] + difference_for_next_line)

    output += sequences[0][-1]

print(output)