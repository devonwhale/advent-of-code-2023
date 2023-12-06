import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

times = list(map(lambda x:int(x), input[0].split(':')[1].split()))
distances = list(map(lambda x:int(x), input[1].split(':')[1].split()))

output = 1

for index in range(0, len(times)):
    speed = 0
    winning_ways = 0
    for time in range(0, times[index]):
        current_potential_distance = (times[index] - time) * speed
        if current_potential_distance > distances[index]:
            winning_ways += 1
        speed += 1
    output *= winning_ways

print(output)