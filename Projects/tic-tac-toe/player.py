
# module that provides mathematical functions and constants
import math
# module that enables generation of random numbers and random selections
import random

# create class blueprint for the players attributes and methods to enable reusability
class Player:
    def __init__(self, team):
        # team is x or o
        self.team = team
    
    # it's important to give each user the chance to have their next move    
    def get_move(self, game):
        # Replace pass with the game functionality
         pass


# Use inheritance to build two extra players that inherit from the base player class
class RandomComputerPlayer(Player):
    def __init__(self, team):
        super().__init__(team)
        
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square
    
class HumanPlayer(Player):
    def __init__(self, team):    
        super().__init__(team)
    
    def get_move(self, game):
        # Human can choose a spot based on
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.team + '\'s turn. Input move (0-9):')
            # Confirm that the correct value is being input
            # Confirm it is an integer, or throw invalid
            # Confirm the spot is available on the board, or say invalid
      
    
    
    