class Node:
    def __init__(self, details):
        name_split = details.split('=')
        self.name = name_split[0].strip()
        details_split = name_split[1].split(',')
        self.left = details_split[0][-3:]
        self.right = details_split[1][-4:-1]

import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

instructions = input[0]

nodes = {}
starting_node = 'AAA'

for line in input[2:]:
    node = Node(line)
    nodes[node.name] = node

current_node = nodes[starting_node]
finished = False
steps = 0
while not finished:
    for char in instructions:
        if current_node.name == 'ZZZ':
            finished = True
            break
        else:
            steps += 1
            if char == 'R':
                current_node = nodes[current_node.right]
            else:
                current_node = nodes[current_node.left]
    else:
        continue
    break

print(steps)
