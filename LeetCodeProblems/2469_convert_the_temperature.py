
# LeetCode 2469

# You are given a non-negative floating point number 
# rounded to two decimal places celsius, that denotes the temperature in Celsius.

# You should convert Celsius into Kelvin and Fahrenheit 
# and return it as an array ans = [kelvin, fahrenheit].

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, (celsius * 1.80) + (32)]