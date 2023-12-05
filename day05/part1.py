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

import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

seeds = list(map(lambda x:int(x), input[0].split(':')[1].split()))

seed_to_soil_map = extract_map(input, 'seed-to-soil map:')
soil_to_fertilizer_map = extract_map(input, 'soil-to-fertilizer map:')
fertilizer_to_water_map = extract_map(input, 'fertilizer-to-water map:')
water_to_light_map = extract_map(input, 'water-to-light map:')
light_to_temperature_map = extract_map(input, 'light-to-temperature map:')
temperature_to_humidity_map = extract_map(input, 'temperature-to-humidity map:')
humidity_to_location_map = extract_map(input, 'humidity-to-location map:')


locations = []
for seed in seeds:
    mapped_soil = process_map(seed, seed_to_soil_map)
    mapped_fertilizer = process_map(mapped_soil, soil_to_fertilizer_map)
    mapped_water = process_map(mapped_fertilizer, fertilizer_to_water_map)
    mapped_light = process_map(mapped_water, water_to_light_map)
    mapped_temperature = process_map(mapped_light, light_to_temperature_map)
    mapped_humidity = process_map(mapped_temperature, temperature_to_humidity_map)
    mapped_location = process_map(mapped_humidity, humidity_to_location_map)
    locations.append(mapped_location)

print(min(locations))
