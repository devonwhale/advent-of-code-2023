class Card:
    def __init__(self, id, winning_numbers, card_numbers):
        self.id = id
        self.winning_numbers = winning_numbers
        self.card_numbers = card_numbers

    def score(self):
        return len(list(self.winning_numbers.intersection(self.card_numbers)))

import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

card_counts = {}
cards = []
output = 0
for line in input:
    split_line = line.split(':')
    id = int(split_line[0].split()[1])
    split_numbers = split_line[1].split('|')
    winning_numbers = set(split_numbers[0].split())
    card_numbers = set(split_numbers[1].split())
    cards.append(Card(id, winning_numbers, card_numbers))
    card_counts[id] = 1

for card in cards:
    for i in range(1, card.score() + 1):
        card_counts[card.id + i] += (1 * card_counts[card.id])

for card, count in card_counts.items():
    output += count
print(output)

