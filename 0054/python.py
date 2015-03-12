from collections import defaultdict


HIGH_CARD = 0
ONE_PAIR = 1
TWO_PAIRS = 2
THREE_OF_A_KIND = 3
STRAIGHT = 4
FLUSH = 5
FULL_HOUSE = 6
FOUR_OF_A_KIND = 7
STRAIGHT_FLUSH = 8
ROYAL_FLUSH = 9

HAND_RANK = {
    HIGH_CARD: 'High card',
    ONE_PAIR: 'One pair',
    TWO_PAIRS: 'Two pairs',
    THREE_OF_A_KIND: 'Three of a kind',
    STRAIGHT: 'Straight',
    FLUSH: 'Flush',
    FULL_HOUSE: 'Full house',
    FOUR_OF_A_KIND: 'Four of a kind',
    STRAIGHT_FLUSH: 'Straight flush',
    ROYAL_FLUSH: 'Royal flush',
}


def straight(face_values):
    if len(face_values) == 5:
        checker = sorted(face_values)
        for i in range(4):
            if checker[i] + 1 != checker[i + 1]:
                return False
        return True
    return False


class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return '{}{}'.format(self.value, self.suit)

    @property
    def face_value(self):
        if self.value == 'T':
            return 10
        if self.value == 'J':
            return 11
        elif self.value == 'Q':
            return 12
        elif self.value == 'K':
            return 13
        elif self.value == 'A':
            return 14
        else:
            return int(self.value)


class Hand(object):
    def __init__(self, cards):
        self.cards = sorted(
            [Card(card[0], card[1]) for card in cards],
            key=lambda card: card.face_value,
            reverse=True,
        )

    def __str__(self):
        return ' '.join([str(card) for card in self.cards])

    def __gt__(self, other):
        """
        Compare hand with the other hand
        """
        if self.type() > other.type():
            return True
        elif self.type() == other.type():
            for i in range(5):
                if self.cards[i] > other.cards[i]:
                    return True
        return False

    def type(self):
        suits = set()
        card_counts = defaultdict(lambda: 0)

        for card in self.cards:
            suits.add(card.suit)
            card_counts[card.face_value] += 1

        has_straight = straight(card_counts)
        has_flush = len(suits) == 1

        if has_flush:
            if has_straight:
                if max(card_counts) == 14:
                    return ROYAL_FLUSH, 14
                else:
                    return STRAIGHT_FLUSH, max(card_counts)
            else:
                return FLUSH, max(card_counts)

        if has_straight:
            return STRAIGHT, max(card_counts)

        best = (HIGH_CARD, self.cards[0].face_value)
        for face_value, copies in card_counts.items():
            if copies == 4:
                best = max(best, (FOUR_OF_A_KIND, face_value))
            if copies == 3:
                if len(card_counts) == 2:
                    best = max(best, (FULL_HOUSE, face_value))
                else:
                    best = max(best, (THREE_OF_A_KIND, face_value))
            if copies == 2:
                if len(card_counts) == 3:
                    best = max(best, (TWO_PAIRS, face_value))
                else:
                    best = max(best, (ONE_PAIR, face_value))

        return best


p1_wins = 0
with open('p054_poker.txt') as hands:
    read_hands = hands.readlines()
    for hand in read_hands:
        cards = hand.split(' ')
        p1_hand = Hand(cards[:5])
        p2_hand = Hand(cards[5:])
        if p1_hand > p2_hand:
            p1_wins += 1

print(p1_wins)
