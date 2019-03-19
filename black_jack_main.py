# Udemy second Mile Stone
# Create simplified black jack game based on modified rules

# You need to create a simple text-based BlackJack game
# The game needs to have one player versus an automated dealer.
# The player can stand or hit.
# The player must be able to pick their betting amount.
# You need to keep track of the player's total money.
# You need to alert the player of wins, losses, or busts, etc


# Class which will take care of players account for the current game
#
class PlayersAccount:
    def __init__(self, player, balance):
        self.player = player
        self.balance = balance

    def balance(self):
        return "You have currently {}$".format(self.balance)

    def player(self):
        return "You are logged as {}".format(self.player)

    def win(self, win):
        self.balance += win

    def loose(self, loose):
        if self.balance - loose < 0:
            print("You SIR, are BUSTED!!!")
        else:
            self.balance -= loose


# # Automated dealer
# class AutomatedDealer(self):
#     def __init__(self):
#         pass


# Take input of player
# How much he wants to take to table, what is his nickname


player = input(str("Hello, what is your name: "))
balance = input("How much you want to take with you to the table: ")


playerLogin = PlayersAccount(player, balance)


print(playerLogin.balance)
print(playerLogin.player)
