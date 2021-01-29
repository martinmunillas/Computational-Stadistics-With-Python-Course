import random

def roll_dice(number_rolls):
    roll_secuence = []

    for _ in range(number_rolls):
        roll = random.randint(1,6)
        roll_secuence.append(roll)

    return roll_secuence


def main(number_rolls, tries):
    rolls =  []
    for _ in range(tries):
        roll_secuence = roll_dice(number_rolls)
        rolls.append(roll_secuence)

    one = 0
    for roll in rolls:
        if 1 in roll:
            one += 1

    probability_one = one / tries
    print(f'Probability of at least one 1: {probability_one}')


if __name__ == '__main__':
    main(3, 10000)