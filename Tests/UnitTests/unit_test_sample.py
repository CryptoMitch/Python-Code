import unittest # Pythons built-in testing framework

class MyTest (unittest.TestCase): # Create individual test cases
# Use the test_ naming convention to show each test method
    def test_addition(self): # Self calls the instance of the class
        # Assertions check whether we get the expected results
        result = 9 + 2
        self.assertEqual(result, 11) # Use assertion to verify the actual results match expected results
    
    def test_subtraction(self):
        result = 2 - 1
        self.assertEqual(result, 1)
        
    def test_multiplication(self):
        result = 3 * 4
        self.assertEqual(result, 12)
        
    def test_modulo(self):
        result = 4 % 2 == 0
        self.assertEqual(result, True)
        

# Use built-in variable to check the current module is being run as the main module 
if __name__ == '__main__':
    unittest.main()
        
    
        
        
    
    