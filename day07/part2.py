class Hand:
    def __init__(self, cards, bet):
        self.cards = cards
        self.bet = int(bet)
        self.hand_type = self.calculate_hand_type()
        self.cards_value = list(map(lambda x:CARD_SCORES[x], list(self.cards)))
    
    def calculate_hand_type(self):
        card_frequency = {}
        for char in self.cards:
            if char in card_frequency:
                card_frequency[char] += 1
            else:
                card_frequency[char] = 1
        
        if 'J' not in card_frequency:
            card_frequency['J'] = 0
        type = 7
        pair_count = 0
        joker_pair = False
        for char, count in card_frequency.items():
            if char == 'J':
                if count == 5:
                    type = 1
                continue
            elif count + card_frequency['J'] == 5:
                type = 1
            elif count + card_frequency['J'] == 4 and type > 2:
                type = 2
            elif self.__calculate_full_house(count, card_frequency) and type > 3:
                type = 3
            elif count + card_frequency['J'] == 3 and type > 4:
                type = 4
            elif count + card_frequency['J'] == 2:
                if count == 2:
                    pair_count += 1
                else:
                    joker_pair = True
        if (pair_count == 2 or (joker_pair and pair_count == 1)) and type > 5:
            type = 5
        elif (pair_count == 1 or joker_pair) and type > 6:
            type = 6
        return HAND_TYPES[type]
    

    def __calculate_full_house(self, count, card_frequency):
        if 'J' in card_frequency:
            if len(card_frequency) == 3:
                return True
        else:
            if len(card_frequency) == 2 and count in [2, 3]:
                return True
        return False
            


CARD_SCORES = {
    'J': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'Q': 12,
    'K': 13,
    'A': 14
}

HAND_TYPES = {
    1: 'Five of a kind',
    2: 'Four of a kind',
    3: 'Full house',
    4: 'Three of a kind',
    5: 'Two pair',
    6: 'One pair',
    7: 'High card'
}

import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

hands = []
for line in input:
    split_line = line.split()
    hands.append(Hand(split_line[0], split_line[1]))

grouped_hands = {
    'Five of a kind': [],
    'Four of a kind': [],
    'Full house': [],
    'Three of a kind': [],
    'Two pair': [],
    'One pair': [],
    'High card': []
}
for hand in hands:
    type = hand.hand_type
    grouped_hands[type].append(hand)

output = 0
idx = len(input)
for type, hand_list in grouped_hands.items():
    if len(hand_list) == 0:
        continue

    if len(hand_list) > 1:
        sorted = False
        while not sorted:
            sorted = True
            for i in range(len(hand_list) - 1):
                for card in range(5):
                    if hand_list[i].cards_value[card] != hand_list[i + 1].cards_value[card]:
                        if hand_list[i].cards_value[card] < hand_list[i + 1].cards_value[card]:
                            smaller_hand = hand_list[i]
                            hand_list[i] = hand_list[i + 1]
                            hand_list[i + 1] = smaller_hand
                            sorted = False
                        break
    sorted_hand_list = hand_list
            

    for hand in sorted_hand_list:
        output += idx * hand.bet
        idx -= 1
    
print(output) 

