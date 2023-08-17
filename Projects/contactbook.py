# Contact Book Project

# Skills Demonstrated: Object Oriented Programming, Encapsulation, Dictionaries, .get() method, Lists, File handling, Input Handling, Control Structures, Strings, Exception handling

class Profile:
    def __init__(self, username, phone_number): # Constructor that initialises the attributes of the profile instance
        self.username = username #This accesses the instance of the class and modifies its attributes
        self.phone_number = phone_number
        
    def __str__(self): # Ensures the profile is represented as a string
        return f"Username: {self.username}, Phone Number: {self.phone_number}"

class ContactBook: # Blueprint for how the instances will behave
    def __init__(self, Profile): # Constructor to initialise the state of the instance
        self.profiles = {} # Empty dictionary of profile instances. Usernames are keys and the profiles are values.
        
    def add_profile(self, profile): # Method to add a profile to the ContactBook, taking two parameters
        self.profiles[profile.username] = profile # Perform the action of adding the profile to the contact book
        
    def search_profile(self, username): # Method that returns a list of all the profiles
        return self.profiles.get(username) # Search for a profile based on the provided username. Gets the profile associated with the provided username.
    
    def list_profiles(self): # List all the profiles in the ContactBook
        return list[self.profiles.values()] # Retrieve the values from the profiles dictionary, convert to list, return the list
    
    def save_to_file(self):
        pass
    
    def load_from_file(self):
        pass
    
    

    
    
