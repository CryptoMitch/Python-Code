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
        
    def eat_porridge(self, temp): # Methods take two parameters
        if self.porridge_temp == temp: # Use porridge_temp to access the bears prefered temp and compare for equality to the actual temp
            return "just right!"
        elif self.porridge_temp > temp: # porridge_temp is the prefered temperature whilst temp is the actual temperature
            return "too hot!"
        else:
            return "too cold."
    
    def try_bed(self, softness):
        if self.bed_softness == softness: # Use porridge_temp to access the bears prefered temp and compare for equality to the actual temp
            return 'just right!'
        elif self.bed_softness > softness: # bed_softness is the prefered softness, whilst softness is the actual softness of the bed
            return 'too hard!'
        else:
            return 'too soft.'

# Entry Point
# High-level logic: Create instances of the Bear class
def main():
    # Create instances of each bear and assign to variables for each bear in the story
    baby_bear= Bear("Baby Bear", 30, 3) # 30 degree porridge and medium bed softness
    mama_bear= Bear("Mama Bear", 40, 5) # 40 degree porridge and soft bed softness
    papa_bear= Bear("Papa Bear", 50, 10) # 50 degree porridge and medium-hard bed softness
    
    print('Goldilocks is in the bears house!\n')
    
    goldilocks_porridge = int(input('How hot do you want your porridge?(Between 0 and 100): '))
    goldilocks_bed = int(input('How soft do you want your bed?(Between 0 and 10): '))
    
    print("Goldilocks tried the porridge:\n")
    print(f"Goldilocks found {baby_bear.name}'s porridge {baby_bear.eat_porridge(goldilocks_porridge)}")
    print(f"Goldilocks found {mama_bear.name}'s porridge {mama_bear.eat_porridge(goldilocks_porridge)}")
    print(f"Goldilocks found {papa_bear.name}'s porridge {papa_bear.eat_porridge(goldilocks_porridge)}")
    
    print("Goldilocks tried the beds: \n")
    print(f"Goldilocks found {baby_bear.name}'s bed {baby_bear.try_bed(goldilocks_bed)}")
    print(f"Goldilocks found {mama_bear.name}'s bed {mama_bear.try_bed(goldilocks_bed)}")
    print(f"Goldilocks found {papa_bear.name}'s bed {papa_bear.try_bed(goldilocks_bed)}")
    
if __name__ == "__main__":
    main()