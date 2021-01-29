import random
import collections

COLORS = ['hearts', 'diamonds', 'clubs', 'spades']
VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def create_deck():
    deck = []
    for color in COLORS:
        for value in VALUES:
            deck.append((color, value))
    return deck

def get_hand(deck, size):
    return random.sample(deck, size)

def main(size, tries):
    deck = create_deck()

    hands = []
    for _ in range(tries):
        hands.append(get_hand(deck, size))
    
    pairs = 0
    for hand in hands:
        values = []
        for card in hand:
            values.append(card[1])
        counter = dict(collections.Counter(values))
        for value in values:
            if counter[value] == 2:
                pairs += 1
                break
    probaility_of_pair = pairs / tries
    print(f'Probability: {probaility_of_pair}')

if __name__ == '__main__':
    main(5, 1000)