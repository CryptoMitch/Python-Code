
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


# Use inheritance to build two extra players that inherits from the base player class