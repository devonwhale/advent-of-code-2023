import itertools

class SpringRow:
    def __init__(self, details):
        split_details = details.split(' ')
        self.springs = split_details[0]
        self.damaged_groups = list(map(lambda x:int(x), split_details[1].split(',')))

    def valid_springs(self):
        count = 0
        
        for potential_sequence in self.__all_combinations():
            broken_occurances = []
            current_length = 0
            for char in potential_sequence:
                if char == '#':
                    current_length += 1
                else:
                    if current_length > 0:
                        broken_occurances.append(current_length)
                        current_length = 0
            
            if current_length > 0:
                broken_occurances.append(current_length)
            
            if broken_occurances == self.damaged_groups:
                count += 1
            
        return count
    
    def __all_combinations(self):
        combinations = []
        for new_symbol in map(iter, itertools.product(['.', '#'], repeat=self.springs.count('?'))):
            combinations.append(''.join(char if char != '?' else next(new_symbol) for char in self.springs))
        return combinations


import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

springs = []
output = 0
for line in input:
    new_row = SpringRow(line)
    springs.append(new_row)
    output += new_row.valid_springs()

print(output)