# 18. [IGA] Exercise 4.6 Returning Values from Custom Functions

"""
Create a custom function that convert from Celsius to Fahrenheit.
Please use the world return in your function.
"""

def ConvertFromCelsiusToFahrenheit(temp):
    try:
        temp = float(temp)
        fahrenheit_value = (temp -32) /1.8
        return f"Your Temp in Fahrenheit = {fahrenheit_value}"
    except ValueError:
        return "Please insert a valid value"

temp = input("Hello Dear to the convert from Celsius to Fahrenheit program \n"
             "Pls insert your temp in numbers only \n"
             "Your Temp is = ")

print(ConvertFromCelsiusToFahrenheit(temp))