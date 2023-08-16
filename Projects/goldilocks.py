# Goldilocks and the Three Bears Simulation

# A fun python challenge created by Mitch Hamilton

# This Python script simulates the famous fairy tale "Goldilocks and the Three Bears."
# Goldilocks visits the bears' house and tries their porridge and beds.
# The bears' characteristics include their names, porridge temperature, and bed softness.
# Goldilocks provides her preferred porridge temperature and bed softness.
# The script then displays humorous responses based on whether Goldilocks likes the porridge and beds.
# Enjoy the playful interactions between Goldilocks and Baby Bear, Mama Bear, and Papa Bear!

#low level logic: class definitions, methods
class Bear: # Superclass that is shared by all bears in the story
    def __init__(self, name, porridge_temp, bed_softness): # Constructor, automatically called when creating a new instance. It sets up the initial state of the object.
        # Instances of the bear class will have access to these methods
        self.name = name
        self.porridge_temp = porridge_temp
        self.bed_softness = bed_softness
        
def eat_porridge(self, porridge_temp):
    if self.porridge_temp == porridge_temp:

# Entry Point
# High-level logic: Create instances of the Bear class
def main():
    baby_bear("Baby Bear", 30, 3) # 30 degree porridge and medium bed softness
    mama_bear("Baby Bear", 40, 5) # 40 degree porridge and soft bed softness
    papa_bear("Papa Bear", 50, 10) # 50 degree porridge and medium-hard bed softness