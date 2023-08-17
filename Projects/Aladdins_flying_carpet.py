# Alladin's Flying Carpet by Mitch Hamilton

# Design a flying carpet that can move in different directions 
# based on Aladdin(the User)'s commands

# Skills: List Comprehension, Decorators, Context Manager, Magic Methods, Async Await, Tuples

# Future ways to improve this code:
    # Enable arrow keys to be used for input
    # Display a visual in the terminal to show the movement

class FlyingCarpet():
    def __init__(self):
        self.position = [0, 0]
        
    def move(self, direction, distance):
        if direction == "up":
            self.position[1] += distance # [1] is the x axis direction
        elif direction == "down":
            self.position[1] -= distance
        elif direction == "left":
            self.position[0] -= distance # [0] is the y axis direction
        elif direction == "right":
            self.position[0] += distance  
    
    def get_position(self):
        return tuple(self.position) #  Converting the list self.position into a tuple to represent a pair of values
        
def main(): # Handle the program's flow of taking user commands and moving the carpet
    carpet = FlyingCarpet() #create instance of the class flying carpet, and assign it to the variable carpet.
    
    print("Flying position initialized at position: ", carpet.get_position())
    
    while True: 
        command = input("Enter the direction you want to move(up, down, left, right) and distance in meters seperated by a space: ")
        
        if command.lower() == "exit":
            break
        
        try: # Begin exception handling
            direction, distance = command.split()
            distance = int(distance)
            
            carpet.move(direction, distance)
        
        except ValueError: # Built in exception class used for incorrect values
            print("Invalid format, please try again with direction and distance separated by space.")
        
        except Exception as e: # Catch any other exceptions and assign to variable e to, then print
            print("An error occured", e)
            
    print("Flying carpet simulation")

if __name__ == "__main__":
    main()
            