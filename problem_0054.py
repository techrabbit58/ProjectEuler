"""This solves problem #54 of Project Euler (https://projecteuler.net).

Poker hands
Problem 54

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest,
in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins;
for example, a pair of eights beats a pair of fives (see example 1 below). But if two RANKS
tie, for example, both players have a pair of queens, then highest cards in each hand are
compared (see example 4 below); if the highest cards tie then the next highest cards are
compared, and so on.

Consider the following five hands dealt to two players:
Hand	 	Player 1	 	  Player 2	 	    Winner
1	 	5H 5C 6S 7S KD      2C 3S 8S 8D TD      Player 2
        Pair of Fives       Pair of Eights
2	 	5D 8C 9S JS AC      2C 5C 7D 8S QH	 	Player 1
       Highest card Ace   Highest card Queen
3	 	2D 9C AS AH AC	 	3D 6D 7D TD QD	 	Player 2
          Three Aces      Flush with Diamonds
4	 	4D 6S 9H QH QC	 	3D 6D 7H QD QS	 	Player 1
        Pair of Queens      Pair of Queens
       Highest card Nine   Highest card Seven
5	 	2H 2D 4C 4D 4S	 	3C 3D 3S 9S 9D	 	Player 1
          Full House          Full House
       With Three Fours    with Three Threes

The file, p054_poker.txt, contains one-thousand random hands dealt to two players. Each line of
the file contains ten cards (separated by a single space): the first five are Player 1's
cards and the last five are Player 2's cards. You can assume that all hands are valid (no
invalid characters or repeated cards), each player's hand is in no specific order,
and in each hand there is a clear winner.

How many hands does Player 1 win?
"""
from itertools import groupby

from helpers import chronometric

ALL_HANDS = 'p054_poker.txt'
RANKS = '23456789TJQKA'
SUITS = 'SDCH'
FRENCH_DECK = ['{}{}'.format(rank, suit) for rank in list(RANKS) for suit in list(SUITS)]


def pairs(hand):
    """Assumes hand to be sorted ascending by rank, then by suit.
    Returns a list of ranks of the pairs that are not part of a triple or a quadruple.
    Result may be an empty list, if no pairs in this hand.
    """
    return [k for k, v in groupby(hand, key=lambda x: x[0]) if len(list(v)) == 2]


def three_of_a_kind(hand):
    """Assumes hand to be sorted ascending by rank, then by suit.
    Returns a list with one triple that is not part of a quadruple.
    Result may be an empty list, if no triple in this hand.
    """
    return [k for k, v in groupby(hand, key=lambda x: x[0]) if len(list(v)) == 3]


def straight(hand):
    """Assumes hand to be sorted ascending by rank, then by suit.
    Returns the hand if all cards have consecutive ranks.
    Result may be an empty list, if the hand does not have this property.
    """
    return hand if RANKS.find(''.join(card[0] for card in hand)) > -1 else []


def flush(hand):
    """
    Returns the hand if all cards are of same suit.
    Result may be an empty list, if SUITS are different.
    """
    return hand if len([k for k, v in groupby(hand, key=lambda x: x[1])
                        if len(list(v)) == 5]
                       ) else []


def full_house(hand):
    """Assumes hand to be sorted ascending by rank, then by suit.
    Returns True if there is one triple and one pair in the hand.
    Returns False, otherwise.
    """
    return bool(three_of_a_kind(hand) and pairs(hand))


def four_of_a_kind(hand):
    """Assumes hand to be sorted ascending by rank, then by suit.
    Returns a list with one quadruple.
    Result may be an empty list, if no quadruple in this hand.
    """
    return [k for k, v in groupby(hand, key=lambda x: x[0]) if len(list(v)) == 4]


def straight_flush(hand):
    """Assumes hand to be sorted ascending by rank, then by suit.
    Returns True if hand is a flush with all cards of same suit.
    Result is False, otherwise.
    """
    return bool(len(flush(hand)) and len(straight(hand)))


def royal_flush(hand):
    """Assumes hand to be sorted ascending by rank, then by suit.
    Returns True if hand is a flush of ranks 'TJQKA'.
    Result may be an empty list, otherwise.
    """
    return ''.join(card[0] for card in hand) == RANKS[-5]


def evaluate(hand):
    """Creates a list of stringified numbers, where each number represents a property of the
    given hand.

    Properties are 0 if the actual property is not there or is obviously evaluated to be 0.
    Properties are ordered descending. That means: lower index is lower value of that property.

    Returns the integer value of all numbers concatenated.
    """
    flush_ = flush(hand)
    four_of_a_kind_ = four_of_a_kind(hand)
    straight_ = straight(hand)
    three_of_a_kind_ = three_of_a_kind(hand)
    pairs_ = pairs(hand)
    return int(''.join([
        '1' if royal_flush(hand) else '0',
        '1' if straight_flush(hand) else '0',
        '1{:02d}'.format(SUITS.index(four_of_a_kind_[0])) if four_of_a_kind_ else '00',
        '1' if full_house(hand) else '0',
        '1{:1d}'.format(SUITS.index(flush_[0][1])) if flush_ else '00',
        '1{:02d}'.format(RANKS.index(straight_[0][0])) if straight_ == hand else '000',
        '1{:02d}'.format(RANKS.index(three_of_a_kind_[0])) if three_of_a_kind_ else '000',
        '1{:02d}{:02d}'.format(
            *sorted([RANKS.index(pairs_[0]), RANKS.index(pairs_[1])])
        ) if len(pairs_) == 2 else '00000',
        '1{:02d}'.format(RANKS.index(pairs_[0])) if len(pairs_) == 1 else '000',
        '{:02d}'.format(FRENCH_DECK.index(hand[4])),
        '{:02d}'.format(FRENCH_DECK.index(hand[3])),
        '{:02d}'.format(FRENCH_DECK.index(hand[2])),
        '{:02d}'.format(FRENCH_DECK.index(hand[1])),
        '{:02d}'.format(FRENCH_DECK.index(hand[0])),
    ]))


@chronometric
def poker_hands():
    # with open(ALL_HANDS) as fp:
    #     games = fp.read().splitlines()
    games = [
        '5H 5C 6S 7S KD      2C 3S 8S 8D TD',
        '5D 8C 9S JS AC      2C 5C 7D 8S QH',
        '2D 9C AS AH AC	 	 3D 6D 7D TD QD',
        '4D 6S 9H QH QC	 	 3D 6D 7H QD QS',
        '2H 2D 4C 4D 4S	 	 3C 3D 3S 9S 9D',
    ]
    player_1_wins = 0
    for n, game in enumerate(games):
        game_cards = game.split()
        players = (
            sorted(game_cards[:5], key=lambda x: FRENCH_DECK.index(x)),
            sorted(game_cards[5:], key=lambda x: FRENCH_DECK.index(x))
        )
        player_1, player_2 = players
        if evaluate(player_1) > evaluate(player_2):
            player_1_wins += 1
    return player_1_wins


def run_application():
    solution, elapsed = poker_hands()
    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
