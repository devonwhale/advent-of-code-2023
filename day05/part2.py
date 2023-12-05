def extract_map(source, map_name):
    index = source.index(map_name) + 1
    map = []
    for i in range(index, len(source)):
        if len(source[i]) == 0:
            break
        rule_set = source[i].split()
        map.append(rule_set)
    return map

def process_map(seed, map):
    for rule_set in map:
        seed_range = range(int(rule_set[1]), int(rule_set[1]) + int(rule_set[2]))
        if seed not in seed_range:
            continue
        return int(rule_set[0]) + (seed - int(rule_set[1]))
    return seed

def process_map_inverted(input, map):
    for rule_set in map:
        source_range_start = int(rule_set[0])
        destination_range_start = int(rule_set[1])
        range_length = int(rule_set[2]) + 1
        range_to_match = range(source_range_start, source_range_start + range_length)
        if input not in range_to_match:
            continue
        values = [destination_range_start, source_range_start]
        if max(values) == destination_range_start:
            new_value = input + (max(values) - min(values))
        else:
            new_value = input - (max(values) - min(values))
        return new_value
    return input

import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

seed_input = list(map(lambda x:int(x), input[0].split(':')[1].split()))
seeds = []
previous_value = -1
largest_value = 0
for seed in seed_input:
    if seed > largest_value:
        largest_value = seed
    if previous_value < 0:
        previous_value = seed
    else:
        seeds.append(range(previous_value, previous_value + seed))
        previous_value = -1

seed_to_soil_map = extract_map(input, 'seed-to-soil map:')
soil_to_fertilizer_map = extract_map(input, 'soil-to-fertilizer map:')
fertilizer_to_water_map = extract_map(input, 'fertilizer-to-water map:')
water_to_light_map = extract_map(input, 'water-to-light map:')
light_to_temperature_map = extract_map(input, 'light-to-temperature map:')
temperature_to_humidity_map = extract_map(input, 'temperature-to-humidity map:')
humidity_to_location_map = extract_map(input, 'humidity-to-location map:')


for i in range(0, largest_value):
    humidity = process_map_inverted(i, humidity_to_location_map)
    temperature = process_map_inverted(humidity, temperature_to_humidity_map)
    light = process_map_inverted(temperature, light_to_temperature_map)
    water = process_map_inverted(light, water_to_light_map)
    fertilizer = process_map_inverted(water, fertilizer_to_water_map)
    soil = process_map_inverted(fertilizer, soil_to_fertilizer_map)
    seed = process_map_inverted(soil, seed_to_soil_map)

    for seed_range in seeds:
        if seed in seed_range:
            print(f'Found {seed} with output {i}')
            break
    else:
        continue
    break
