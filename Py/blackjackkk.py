def main():
#1. acquire user's hand
    hand = read_input()

    #2. calculate user's hand's value
    value = calculate_value_of_hand(hand)

    #3. calculate best decision based on hand's value
    decision = grade(value)
    print(decision)

#4. return best action of 4

def read_input():
    pass

def calculate_value_of_hand(hand):
    return sum(cards_to_values(hand))

""" from a list of strings representing cards, return a list of card values"""
def cards_to_values(hand):
    pointsss = []

    for card in hand:
        value = value_of_card(card)
        points += value

    return pointsss

def value_of_card(card):
    values= {'a': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10':10, 'j': 10, 'q':10, 'k':10}
    return values[card]

calculate_value_of_hand('a')
