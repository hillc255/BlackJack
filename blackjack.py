import random
import string

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
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "J", "Q", "K"]

    def __init__(self, suits, ranks):
        """Sets up individual card"""
        self.suits = suits
        self.ranks = ranks

    def __str__(self):
        """Prints the individual card"""
        return self.suits + self.ranks


class Deck(object):

    def __init__(self):
        """Calls populate method and shuffles deck."""
        print("Card deck opened.")
        self.cards = []

    def populate(self):
        """Populates the deck with cards"""
        for rank in Card.ranks:
            for suit in Card.suits:
                self.cards.append(Card(rank,suit))
        print('Dealer populated deck.')

    def __str__(self):
        """Converts location to string value"""
        print('Deck of shuffled cards.')
        res = []
        for card in self.cards:
            res.append(str(card))
        return ", ".join(res)

    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)
        print('Dealer shuffled deck.')


class Player(object):

    #chips = 0
    #bet = 0
    #game_on = True

    def __init__(self):
        """Tracks user bet binput and chips"""
        self.game_on = True
        self.chips = 0
        self.bet = 0
        self.sum = 0

    def playerBuysChips(self):
        if self.game_on is True:
            while True:
                try:
                    self.chips = int(input('Player, how many chips would you like to buy? '))
                except ValueError:
                    print("Invalid entry. Try again")
                    continue
                else:
                    if self.chips == 0:
                        print("Chip(s) purchased must be greater than 0.  Try again.")
                        continue
                break
        return self.chips

    def playerPlacesBet(self):
        #successful chips purchased - ready to place bet
        while not ((self.chips <= 0) & (self.game_on is True)):
                while True:
                    try:
                        self.bet = int(input('Player, what\'s your bet? '))
                    except ValueError:
                        print("Invalid entry. Try again")
                        continue
                    else:
                        if self.bet == 0:
                            print("Bet must be greater than 0.  Try again.")
                            continue
                    break
                    #successful bet entered - make sure there are chips
                self.sum = self.chips - self.bet
                if self.sum < 0:
                    print('Invalid bet. Please try again.')
                    self.sum == 0
                else:
                    self.chips = self.sum
                    print(f'You bet {self.bet} with {self.chips} chip(s) remaining.')
                    print('Let\'s play.')
                    self.bet = 0
                    self.game_on = False
                    break
        return

    def replay(self):
        self.replayGame = input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
        if self.replayGame == 'y':
            Player.playerBuysChips().game_on = True
            Player.playerBuysChips(self)
        else:
            return



class Dealer(object):

    def __init__(self,cards):
        '''Dealer deals a hand and counts total'''
        self.playerCards = []
        self.dealerCards = []
        self.usedDeck = []
        self.usedDeck = cards

    def __str__(self):
        '''Card removed from deck'''
        print('Used deck')
        res2 = []
        for card2 in self.usedDeck:
            res2.append(str(card2))
        return ", ".join(res2)

    def cardRemoveSuit(self, playerCards):
        '''Remove the suits from the list'''
        temp = []
        self.temp = self.playerCards
        print('\nStripped out suits')
        temp2 = []
        for i in self.temp:
            temp2.append((str(i)[ :-1]))
        print(", ".join(temp2))
        #return temp2

        print('\nReplace J,Q,K with 10')
    '''
   # def cardCount(self, temp2):
        #Replace JQK with 10
        temp3 = []
        temp3 = temp2
        temp4 = []
        for j in temp3:
            if j in ['J','Q','K']:
                 temp4.append([j.replace(j, '10') for j in temp3[j]])
        print(", ".join(temp4))
    '''

    def dealCard(self, usedDeck):
        self.item = self.usedDeck.pop(0)
        print('Single card removed from deck')
        print(str(self.item))
        return self.item, self.usedDeck

    def playerHand(self):
        print("Player\'s hand: Add card and print")
        self.playerCards.append(self.item)
        pc = []
        for pcard in self.playerCards:
            pc.append(str(pcard))
        print( ", ".join(pc))

    def dealerHand(self):
        print("Dealer\'s hand: Add card and print")
        self.dealerCards.append(self.item)
        dc = []
        for dcard in self.dealerCards:
            dc.append(str(dcard))
        print(", ".join(dc))

    def setUpGame(self):
        print("\nDealer deals self 2 cards and displays 1")
        self.dealCard(self.usedDeck)
        self.dealerHand()
        self.dealCard(self.usedDeck)
        self.dealerHand()

        print('------------------')

        for i in self.dealerCards[:1]:
            print(f'Dealer Card 1: {str(i)}')
        for j in self.dealerCards[1:2]:
            print(f'Dealer Card 2: {str(j)}')
        print('Dealer Card 2: Blank')

        print('------------------')

        print("Dealer deals player 2 cards and displays both")
        self.dealCard(self.usedDeck)
        self.playerHand()
        self.dealCard(self.usedDeck)
        self.playerHand()

        print('------------------')

        for i in self.playerCards[:1]:
            print(f'Player Card 1: {str(i)}')
        for j in self.playerCards[1:2]:
            print(f'Player Card 2: {str(j)}')

        print('------------------')

if __name__ == "__main__":

    print("Welcome to BlackJack!\n")

    #Objects being used
    my_deck = Deck()
    my_player = Player()
    my_dealer = Dealer(my_deck.cards)

    #Player buys chips and places bet
    #my_player.playerBuysChips()
    #my_player.playerPlacesBet()

    #Preparing deck
    my_deck.populate()
    my_deck.shuffle()
    print(my_deck)

    #Deal cards for dealer and player
    my_dealer.setUpGame()

    # my_player.replay() #not quite working

    #sum: print("The sum of values is {0}".format(sum(n)))

    '''
    #Remove a card from the deck with pop and print it
    my_dealer.dealCard(my_deck.cards)
    #Add item removed from deck to player's hand and print player's hand
    my_dealer.playerHand()
    #print remaining cards in deck
    print(my_dealer)

    #Remove a second card from the deck with pop and print it
    my_dealer.dealCard(my_dealer.usedDeck)
    #Add second item removed from deck to player's hand and print player's hand
    my_dealer.playerHand()
    #print remaining cards in deck
    print(my_dealer)

    #Remove a third card from the deck with pop and print it
    my_dealer.dealCard(my_dealer.usedDeck)
    #Add third item removed from deck to player's hand and print player's hand
    my_dealer.playerHand()
    #print remaining cards in deck
    print(my_dealer)

    #Remove a fourth card from the deck with pop and print it
    my_dealer.dealCard(my_dealer.usedDeck)
    #Add fourth removed from deck to player's hand and print player's hand
    my_dealer.playerHand()
    #print remaining cards in deck
    print(my_dealer)
    '''
    '''
    #Remove a third card from the deck with pop and print it
    my_dealer.dealCard(my_dealer.usedDeck)
    #Add third item removed from deck to dealer's hand and print dealer's hand
    my_dealer.dealerHand()
    #print remaining cards in deck
    print(my_dealer)

    #Remove a fourth card from the deck with pop and print it
    my_dealer.dealCard(my_dealer.usedDeck)
    #Add fourth item removed from deck to dealer's hand and print dealer's hand
    my_dealer.dealerHand()
    #print remaining cards in deck
    print(my_dealer)
     
    '''
    #strip suits from player's or dealer's hand
    my_dealer.cardRemoveSuit(my_dealer.playerCards)

    #replace J,Q, K by 10
    #my_dealer.cardCount(my_dealer.temp2)

    print('\nGame over')


'''
done 1.Create a deck of 52 cards
done 2.Shuffle the deck
done 3.Ask the Player for their bet
done 4.Make sure that the Player's bet does not exceed their available chips
done 5.Deal two cards to the Dealer and two cards to the Player
done 6.Show only one of the Dealer's cards, the other remains hidden
done 7.Show both of the Player's cards
8.Ask the Player if they wish to Hit, and take another card
9.If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
10.If a Player Stands, play the Dealer's hand. The dealer will always
11.Hit until the Dealer's value meets or exceeds 17
12.Determine the winner and adjust the Player's chips accordingly
13.Ask the Player if they'd like to play again
'''