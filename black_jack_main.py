# Udemy second Mile Stone
# Create simplified black jack game based on modified rules

# You need to create a simple text-based BlackJack game
# The game needs to have one player versus an automated dealer.
# The player can stand or hit.
# The player must be able to pick their betting amount.
# You need to keep track of the player"s total money.
# You need to alert the player of wins, losses, or busts, etc

from deck_of_cards import deck_of_cards
import random
import time

# Globally accessible cards of player / computer
# So we can reset it every round if necessary
player_cards = {}
computer_cards = {}


# Class which will take care of players account for the current game
class PlayersAccount:
    def __init__(self, player, balance):
        self.player = player
        self.balance = balance

    def balance(self):
        return "You have currently {}$".format(self.balance)

    def player(self):
        return "You are logged as {}".format(self.player)


# Automated dealer
# Cards of computer, cards of player
# Several methods :
# 1. Initial deal
# 2. Hit
# 3. Stay
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

    # Logic of computer
    # Computer draws a card every time when he is below player
    # Game ends if computer has 21 as computer wons
    # Game ends if computer has >21 as computer lose
    # Game ends if computer has more than player as players lose
    def computer_moves(self):
        global bet
        global balance
        print("You decided to stay, now its my turn to beat you!")
        print("I have: {} of total value {}".format(", ".join(self.computer_cards), self.card_value_computer()))
        while self.card_value_player() >= self.card_value_computer():
            print("Computer is drawing a card ... ")
            time.sleep(3)
            self.hit_computer()
            print("I have: {} of total value {}".format(", ".join(self.computer_cards), self.card_value_computer()))
            if self.card_value_computer() == 21:
                balance = int(balance) - int(bet)
                print("Computer have 21, you have lost {}$".format(bet))
                print("Your current account balance is {}$".format(balance))
                break
            elif self.card_value_computer() > 21:
                balance = int(balance) + int(bet)
                print("Computer is over 21, you have won {}$".format(bet))
                print("Your current account balance is {}$".format(balance))
                break
            elif self.card_value_player() < self.card_value_computer():
                balance = int(balance) - int(bet)
                print("Computer have {} and you manage to do only {}".format(self.card_value_computer(), self.card_value_player()))
                print("You have lost {}$ in this round!!!".format(bet))
                print("Your current account balance is {}$".format(balance))

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

    # Print current status of players cards and sum of their value
    def value_print(self):
        return "You have {} of total value {}".format(", ".join(self.player_cards), self.card_value_player())

    # Define method which will check if player did 21 = WIN or >21 = LOSE
    def player_win_or_loose(self):
        global keep_going, bet, balance, busted
        if self.card_value_player() > 21:
            print("You have lost the game!!")
            print("You have lost {}$".format(bet))
            balance = int(balance) - int(bet)
            print("Your current account balance is {}$".format(balance))
            if balance == 0:
                print("BUSTED")
                print("Game ended, you have currently {}$ on your account".format(balance))
                print("Bye {}, come again!".format(player))
                busted = True

            keep_going = False

        if self.card_value_player() == 21:
            print("You have won the game!!")
            print("You have won {}$".format(bet))
            balance = int(balance) + int(bet)
            print("Your current account balance is {}$".format(balance))
            keep_going = False


# Take input of player
# How much he wants to take to table, what is his nickname
#
# INITIAL SETTING OF THE GAME:
#
player = input(str("Hello, what is your name: \n"))

while True:
    try:
        balance = int(input("How much $ you want to take with you to the table: \n"))
        if balance > 0:
            print("Hello {} you have {}$ on your account balance.".format(player, balance))
            break
        else:
            print("You can't take less than 1$ to a table, silly")
    except ValueError:
        print("I do not except anything else than coins!")
        print("Try again..")

# Initialize class for players account and dealer
playerLogin = PlayersAccount(player, balance)
deal_the_cards = AutomatedDealer(deck_of_cards, player_cards, computer_cards)

# Variables to keep game going
next_game = ""
hit_or_stay = ""
keep_going = True
possible_bet = False
busted = False

while not busted:
    next_game = input("Do you wish to play another round? Yes/No: \n")
    if next_game == "Yes":
        computer_cards.clear()
        player_cards.clear()
        # Reset variable checking if bet is possible
        possible_bet = False
        while not possible_bet:
            try:
                print("You have currently {}$ on your account".format(balance))
                bet = int(input("How much do you wish to bet? \n"))
                if bet > balance:
                    print("The bet is too big, Your bankroll is not big enough")
                    continue
            except ValueError:
                print("I do not except anything else than coins!")
                print("Try again..")
                continue
            else:
                print("You bet {}$ for current round. Good luck".format(bet))
                possible_bet = True

        deal_the_cards.initial_deal()
        keep_going = True
        while keep_going:
            deal_the_cards.player_win_or_loose()
            hit_or_stay = input("Do you wish to hit another card or will you stay? Hit/Stay: \n")
            if hit_or_stay == "Hit":
                deal_the_cards.hit_player()
                print(deal_the_cards.value_print())
                deal_the_cards.player_win_or_loose()
            elif hit_or_stay == "Stay":
                deal_the_cards.stay()
                print(deal_the_cards.value_print())
                deal_the_cards.computer_moves()
                break

    elif next_game == "No":
        print("Game ended, you have currently {}$ on your account".format(balance))
        print("Bye {}, come again!".format(player))
        break
