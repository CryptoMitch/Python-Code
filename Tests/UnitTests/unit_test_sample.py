import unittest # Pythons built-in testing framework

class MyTest (unittest.TestCase): # Create individual test cases
# Use the test_ naming convention to show each test method
    def test_addition(self): # Self calls the instance of the class
        # Assertions check whether we get the expected results
        result = 9 + 2
        self.assertEqual(result, 11) # Use assertion to verify the actual results match expected results
        print(f'Addition result of {result} is correct')
    
    def test_subtraction(self):
        result = 2 - 1
        self.assertEqual(result, 1)
        print(f'Subtraction result of {result} is correct')
        
    def test_multiplication(self):
        result = 3 * 4
        self.assertEqual(result, 12)
        print(f'Multiplication result of {result} is correct')
        
    def test_modulo(self):
        result = 4 % 2
        self.assertTrue(result == 0)
        print(f'Modulo result of {result} is correct')
        
# Intentionally Failing Test Cases
    def test_addition_fail(self):
        result = 1 + 1
        self.assertEqual(result, 3) # Intentional Failing Test Case
        
    def test_subtraction_fail(self):
        result = 3 - 2
        self.assertEqual(result, 4) # Intentional Failing Test Case

        
# Use built-in variable to check the current module is being run as the main module 
if __name__ == '__main__':
    unittest.main()
        
    
        
        
    
    