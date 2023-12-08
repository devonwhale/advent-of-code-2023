class Node:
    def __init__(self, details):
        name_split = details.split('=')
        self.name = name_split[0].strip()
        details_split = name_split[1].split(',')
        self.left = details_split[0][-3:]
        self.right = details_split[1][-4:-1]

import os
from math import lcm
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

instructions = input[0]

nodes = {}

for line in input[2:]:
    node = Node(line)
    nodes[node.name] = node

nodes_to_evaluate = []
for node in nodes.items():
    if node[0][-1] == 'A':
        nodes_to_evaluate.append(node[1])
steps_to_z = []

for node in nodes_to_evaluate:
    current_node = node
    steps = 0
    node_complete = False
    while not node_complete:
        for char in instructions:
            finished = 0
            steps += 1 
            if char == 'R':
                current_node = nodes[current_node.right]
            else:
                current_node = nodes[current_node.left]
            
            if current_node.name[-1] == 'Z':
                steps_to_z.append(steps)
                node_complete = True
                break
        

print(lcm(*steps_to_z))
