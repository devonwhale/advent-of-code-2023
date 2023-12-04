import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

output = 0
for line in input:
    split_line = line.split(':')
    id = split_line[0]
    split_numbers = split_line[1].split('|')
    winning_numbers = set(split_numbers[0].split())
    card_numbers = set(split_numbers[1].split())

    winners = list(winning_numbers.intersection(card_numbers))
    card_score = 0
    for winner in range(0, len(winners)):
        if card_score == 0:
            card_score = 1
        else:
            card_score = card_score * 2
    output += card_score

print(output)

