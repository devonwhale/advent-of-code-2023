import os
import re
input = open(os.path.join(os.path.dirname(__file__), "sample_input_2.txt"), 'r').read().splitlines()

values = []

for line in input:
    first_digit = re.search("[0-9]", line).group()
    second_digit = re.search("[0-9]", line[::-1]).group()
    values.append(int(f'{first_digit}{second_digit}'))

output = 0
for value in values:
    output = output + value

print(output)