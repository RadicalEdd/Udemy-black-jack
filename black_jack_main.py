# Udemy second Mile Stone
# Create simplified black jack game based on modified rules

# You need to create a simple text-based BlackJack game
# The game needs to have one player versus an automated dealer.
# The player can stand or hit.
# The player must be able to pick their betting amount.
# You need to keep track of the player"s total money.
# You need to alert the player of wins, losses, or busts, etc

#
#
#   print whole dictionary
#       for k, v in self.player_cards.items():
#       print(k, v)
#

from deck_of_cards import deck_of_cards
import random

# Globally accessible cards of player / computer
# So we can reset it every round if necessary
player_cards = {}
computer_cards = {}


# Class which will take care of players account for the current game
# Included bet method
class PlayersAccount:
    def __init__(self, player, balance):
        self.player = player
        self.balance = balance

    def balance(self):
        return "You have currently {}$".format(self.balance)

    def player(self):
        return "You are logged as {}".format(self.player)

    def bet(self):
        pass

    def pot(self):
        pass

    def win(self, win):
        self.balance += win

    def loose(self, loose):
        if self.balance - loose < 0:
            print("You SIR, are BUSTED!!!")
        else:
            self.balance -= loose


# Automated dealer
# Cards of computer, cards of player
# Several methods :
# 1. Initial deal
# 2. Hit
# 3. Stay
#
class AutomatedDealer:
    # Globally accessible dictionary of player's cards
    global player_cards
    global computer_cards

    playing_cards = deck_of_cards
    # Computer + Human cards variables
    dealt_card = []
    dealt_value = []

    def __init__(self, deck_of_cards, player_cards, computer_cards):
        self.deck_of_cards = deck_of_cards
        self.player_cards = player_cards
        self.computer_cards = computer_cards

    # Deal two cards for player and one for computer
    def initial_deal(self):
        print("=== GAME STARTS ===")
        self.hit_player()
        self.hit_player()
        self.hit_computer()
        print("Your cards: {} of total value {}".format(", ".join(self.player_cards), self.card_value_player()))
        print("Computer cards: {} of total value {}".format(", ".join(self.computer_cards), self.card_value_computer()))

    # Computer draws a card
    # Computers cards are updated
    # A card is removed from a deck
    def hit_computer(self):
        dealt_card, dealt_value = random.choice(list(self.playing_cards.items()))
        self.computer_cards.update({dealt_card: dealt_value})
        del self.playing_cards[dealt_card]
        return self.computer_cards

    # Player draws a card
    # Players cards are updated
    # A card is removed from a deck
    def hit_player(self):
        dealt_card, dealt_value = random.choice(list(self.playing_cards.items()))
        self.player_cards.update({dealt_card: dealt_value})
        del self.playing_cards[dealt_card]
        return self.player_cards

    # When player decides to stay, return value of his cards and let computer make its move
    def stay(self):
        return "You decided to stay, value of your cards is: {}".format(self.card_value_player())

    # Return sum of cards owned by player
    def card_value_player(self):
        return sum(self.player_cards.values())

    # Return sum of cards owned by computer
    def card_value_computer(self):
        return sum(self.computer_cards.values())

    def value_print(self):
        return "You have {} of total value {}".format(", ".join(self.player_cards), self.card_value_player())

    # Define method which will check if player did 21 = WIN or >21 = LOSE
    def win_or_loose(self):
        global keep_going
        if self.card_value_player() > 21:
            print("You have lost the game!!")
            # TODO
            # Add function for betting
            # Won => + bank
            print("You have lost {xx$}")
            keep_going = False

        elif self.card_value_player() == 21:
            print("You have won the game!!")
            # TODO
            # Add function for betting
            # Lost => - bank
            keep_going = False


# Take input of player
# How much he wants to take to table, what is his nickname
#
# INITIAL SETTING OF THE GAME:
#
player = input(str("Hello, what is your name: \n"))

while True:
    try:
        balance = int(input("How much you want to take with you to the table: \n"))
    except ValueError:
        print("I do not except anything else than coins!")
        print("Try again..")
        continue
    else:
        print("Hello {} you have {}$ on your account balance.".format(player, balance))
        break

playerLogin = PlayersAccount(player, balance)
deal_the_cards = AutomatedDealer(deck_of_cards, player_cards, computer_cards)

# print(playerLogin.balance)
# print(playerLogin.player)

next_game = True
keep_going = True
hit_or_stay = ""


while True:
    next_game = input("Do you wish to play another round? Yes/No: \n")
    if next_game == "Yes":
        computer_cards.clear()
        player_cards.clear()
        deal_the_cards.initial_deal()
        keep_going = True
        while keep_going:
            hit_or_stay = input("Do you wish to hit another card or will you stay? Hit/Stay: \n")
            if hit_or_stay == "Hit":
                deal_the_cards.hit_player()
                print(deal_the_cards.value_print())
                deal_the_cards.win_or_loose()
            elif hit_or_stay == "Stay":
                deal_the_cards.stay()
                break

    elif next_game == "No":
        print("Game ended, you have currently {}$ on your account".format(balance))
        print("Bye {}, come again!".format(player))
        break
