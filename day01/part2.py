import os
import re

REGEX = "[0-9]|(zero)|(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)"
REGEX_REVERSED = "[0-9]|(orez)|(eno)|(owt)|(eerht)|(ruof)|(evif)|(xis)|(neves)|(thgie)|(enin)"
NUMERIC_DICTIONARY = {
    'zero': 0, 'orez': 1,
    'one': 1, 'eno': 1,
    'two': 2, 'owt': 2,
    'three': 3, 'eerht': 3,
    'four': 4, 'ruof': 4,
    'five': 5, 'evif': 5,
    'six': 6, 'xis': 6,
    'seven': 7, 'neves': 7,
    'eight': 8, 'thgie': 8,
    'nine': 9, 'enin': 9
}

def parse_line(line):
    first_digit = re.search(REGEX, line).group()
    second_digit = re.search(REGEX_REVERSED, line[::-1]).group()
    return int(f'{map_numeric_word(first_digit)}{map_numeric_word(second_digit)}')

def map_numeric_word(word):
    if len(word) == 1:
        return word
    return NUMERIC_DICTIONARY[word]

input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

values = []

for line in input:
    values.append(parse_line(line))

output = 0
for value in values:
    output = output + value

print(output)