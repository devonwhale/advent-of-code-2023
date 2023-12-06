import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

times = list(map(lambda x:int(x), input[0].split(':')[1].split()))
time = ''
for t in times:
    time += f'{t}'
distances = list(map(lambda x:int(x), input[1].split(':')[1].split()))
distance = ''
for d in distances:
    distance += f'{d}'

time = int(time)
distance = int(distance)

speed = 0
winning_ways = 0
for t in range(0, time):
    current_potential_distance = (time - t) * speed
    if current_potential_distance > distance:
        winning_ways += 1
    speed += 1

print(winning_ways)