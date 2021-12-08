import math
import random

class Player:
    def __init__(self,letter):
        #letter is x or o
        self.letter=letter

    #we want all players to get their next move given a game
    def get_move(self,game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square= random.choice(game.available_moves())

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self,game):
        valid_squre=False
        val= None
        while not valid_squre:
            square=input(self.letter + '\'s turn. Input move (0-9):')
            # we are going to check that this is a correct value by trying to cast
            # it to an integer, and if its not, the we say its invalid
            # if that spot is not available on the board , we also say its invalid 
            try:
                val=int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_squre= True # if these are successful, yay
            except ValueError:
                print('Invalid Square.Try Again')
        return val
        