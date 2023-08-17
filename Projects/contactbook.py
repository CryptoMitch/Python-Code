# Contact Book Project

# Skills Demonstrated: Object Oriented Programming, File handling, Input Handling, Control Structures, Strings, Dictionaries, Exception handling

class Profile:
    def __init__(self, username, phone_number): # Constructor that initialises the attributes of the profile instance
        self.username = username #This accesses the instance of the class and modifies its attributes
        self.phone_number = phone_number
        
    def __str__(self): # Ensures the profile is represented as a string
        return f"Username: {self.username}, Phone Number: {self.phone_number}"

class ContactBook: # Blueprint for how the instances will behave
    def __init__(self, Profile): # Constructor to initialise the state of the instance
        self.profiles = {} 
        
    def add_profile(self, profile): # Method to add a profile to the ContactBook
        pass
        
    def search_profile(): # Method that returns a list of all the profiles
        pass
    
    def list_profiles(self):
        pass
    
    def save_to_file(self):
        pass
    
    
