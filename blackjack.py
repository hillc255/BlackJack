import random

'''
Title:        BlackJack Game
# Date:       1/13/2020
Author:       Claudia Hill
Purpose:      Create BlackJack Game with Python
              Milestone 2 - Udemy Python Bootcamp
Description:  Original code in PyCharm IDE
'''

class Card(object):

    suits = ["♠", "♣", "♥", "♦"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "ace", "jack", "queen", "king"]

    def __init__(self, suits, ranks):
        """Sets up individual card"""
        self.suits = suits
        self.ranks = ranks

    def __str__(self):
        """Prints the individual card"""
        return self.suits + " " + self.ranks


class Deck(object):

    def __init__(self):
        """Calls populate method and shuffles deck."""
        print("Here is the deck")
        self.cards = []
        self.populate()
        self.shuffle()

    def populate(self):
        """Populates the deck with cards"""
        for rank in Card.ranks:
            for suit in Card.suits:
                self.cards.append(Card(rank,suit))

    def __str__(self):
        """Converts location to string value"""
        res = []
        for card in self.cards:
            res.append(str(card))
        return "\n".join(res)

    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)


class Player():
    pass


class Dealer():
    pass



if __name__ == "__main__":

    print("Welcome to BlackJack!\n")

    #print entire deck
    print("Calling Deck with Cards\n")
    deck = Deck()
    print(deck)

    #Begin game
    #print player's first two cards face up
    #remove these from the deck
    #print dealer first card, save dealer second card not display
    #remove these cards from the deck

    #ask player if stay or hit

    #stay
    #if player stays
    # turn over dealer's second card and count totals
    # count player's totals
    #whoever is closest to 21 wins
    #if someone over - they lose

    #hit
    #if player says hit
    # add card to player - remove card from deck
    # total card points
    # if ace - player chooses 1 or 11 points
    # if over 21 players loses
    #continue until player says stay





