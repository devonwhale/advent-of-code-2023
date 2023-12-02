class Game:
    def __init__(self, details):
        self.id = int(details.split(':')[0].split()[-1])
        self.sets = details.split(':')[1].split(';')

    def within_allowable_cube_count(self, colour, allowable_count):
        for set in self.sets:
            correctly_coloured_cubes = [cubes for cubes in set.split(',') if colour in cubes]
            if len(correctly_coloured_cubes) == 1:
                if int(correctly_coloured_cubes[0].split()[0]) > allowable_count:
                    return False
        return True
    
    def smallest_possible_cube_count(self, colour):
        smallest_possible_count = 0
        for set in self.sets:
            cube_count = [cubes for cubes in set.split(',') if colour in cubes]
            if len(cube_count) == 1:
                count = int(cube_count[0].split()[0])
                if count > smallest_possible_count:
                    smallest_possible_count = count
        return smallest_possible_count

import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

output = 0

for line in input:
    game = Game(line)
    power = game.smallest_possible_cube_count('red') * game.smallest_possible_cube_count('green') * game.smallest_possible_cube_count('blue')
    output += power

print(output)