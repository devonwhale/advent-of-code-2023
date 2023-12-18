import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

x = 0
y = 0
edge_len = 0

# https://en.wikipedia.org/wiki/Shoelace_formula
corners = []

for line in input:
    hex = line.split(' ')[-1][2:-1]
    distance = int(hex[:-1], 16)
    if hex[-1] == '0':
        x += 1 * distance
    elif hex[-1] == '3':
        y += 1 * distance
    elif hex[-1] == '2':
        x -= 1 * distance
    elif hex[-1] == '1':
        y -= 1 * distance
    edge_len += distance
    corners.append((x, y))


final_corner_index = len(corners) - 1
x_by_next_y = corners[final_corner_index][0] * corners[0][1]
y_by_next_x = corners[0][0] * corners[final_corner_index][1]
for index in range(0, final_corner_index):
    x_by_next_y += corners[index][0] * corners[index + 1][1]
    y_by_next_x += corners[index][1] * corners[index + 1][0]

internal_area = abs(x_by_next_y - y_by_next_x) / 2

# https://en.wikipedia.org/wiki/Pick%27s_theorem
print(internal_area + (edge_len / 2) + 1)