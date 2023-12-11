import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

empty_rows = []
empty_columns = []
galaxy_locations = []

for column_count in range(0, len(input[0])):
    column_empty = True
    for row_count in range(0, len(input)):
        if input[row_count][column_count] == '#':
            column_empty = False
            galaxy_locations.append([row_count, column_count])
    if column_empty:
        empty_columns.append(column_count)

for row_count in range(0, len(input)):
    row_empty = True
    for column_count in range(0, len(input[0])):
        if input[row_count][column_count] == '#':
            row_empty = False
    if row_empty:
        empty_rows.append(row_count)

transformed_galaxy_locations = []
for galaxy in galaxy_locations:
    row = galaxy[0]
    column = galaxy[1]
    additional_rows = len([x for x in empty_rows if x < row])
    additional_columns = len([x for x in empty_columns if x < column])
    transformed_galaxy_locations.append([row + additional_rows, column + additional_columns])

locations_to_calculate = transformed_galaxy_locations.copy()

output = 0

for galaxy in transformed_galaxy_locations:
    locations_to_calculate.remove(galaxy)
    for location in locations_to_calculate:
        output += abs(galaxy[0] - location[0]) + abs(galaxy[1] - location[1])

print(output)