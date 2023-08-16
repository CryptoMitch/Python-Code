import unittest # Pythons built-in testing framework

class MyTest (unittest.TestCase): # Create individual test cases
# Use the test_ naming convention to show each test method
    def test_addition(self) # Self calls the instance of the class
    # Assertions check whether we get the expected results
    result = 2 + 2
    self.assertEqual(result, 4) # Use assertion to verify the actual results match expected results
    
    
    