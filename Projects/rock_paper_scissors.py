# Tutorial followed found here: https://www.youtube.com/watch?v=8ext9G7xspg
# Timestamp: 21:14 of the video

# Because this challenge was too simple I added two extra non-sanctioned weapons to the game.
# Lizard and Spock were added to the game.

# View the instructions to the game here: https://adams.osu.edu/sites/adams/files/imce/4-H/STEM_Camp/Rock%20Paper%20Scissors%20Lizard%20Spock.pdf

# The rules of Rock-paper-scissors-lizard-Spock are:
    # Scissors cut paper = s > p
    # Paper covers rock = p > r
    # Rock breaks scissors r > s
    # Rock crushes lizard = r > l
    # Lizard poisons Spock = l > sp
    # Spock smashes (or melts) scissors = sp > s
    # Scissors decapitate lizard = s > l
    # Lizard eats paper = l > p
    # Paper disproves Spock = p > sp
    # Spock vaporizes rock = sp > r
    


import random

def playGame():
    user = input("Choose: 'r' for rock, 'p' for paper, 's' for scissors, 'l' for lizard, or 'sp' for Spock: ")
    computer = random.choice(['r', 'p', 's', 'l', 'sp'])
    
    # If user and the computer have the same choice, the game is a tie
    if user == computer:
        return "It's a tie!"
    
    if is_win(user, computer):
        return "You win!"
    
    return 'You lose!'
    
    # The rules of Rock-paper-scissors-lizard-Spock are:
    # s > p, p > r, r > s, r > l, l > sp, sp > s, s > l, l > p, p > sp, sp > r
        # Scissors cut paper = s > p
        # Paper covers rock = p > r
        # Rock breaks scissors r > s
        # Rock crushes lizard = r > l
        # Lizard poisons Spock = l > sp
        # Spock smashes (or melts) scissors = sp > s
        # Scissors decapitate lizard = s > l
        # Lizard eats paper = l > p
        # Paper disproves Spock = p > sp
        # Spock vaporizes rock = sp > r

# Win Conditions
def is_win(player, worldchampion):
    # return true if player wins    
    if (player == 's' and worldchampion =='p') or \
        (player == 'p' and worldchampion == 'r') or \
        (player == 'r' and worldchampion == 's') or \
        (player == 'r' and worldchampion == 'l') or \
        (player == 'l' and worldchampion == 'sp') or \
        (player == 'sp' and worldchampion == 's') or \
        (player == 's' and worldchampion == 'l') or \
        (player == 'l' and worldchampion == 'p') or \
        (player == 'p' and worldchampion == 'sp') or \
        (player == 'sp' and worldchampion == 'r'):
        return True
    
# Call the playGame function to start the game
result = playGame()
print(result)