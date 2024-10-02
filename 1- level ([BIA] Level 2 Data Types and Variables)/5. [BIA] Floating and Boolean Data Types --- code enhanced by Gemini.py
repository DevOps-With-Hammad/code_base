# 5. [BIA] Floating and Boolean Data Types

# Assigning values and checking data types
num1 = 3.14  # Float (decimal number)
print(f"num1 is of type: {type(num1)}")

num2 = 22  # Integer (whole number)
print(f"num2 is of type: {type(num2)}")

num3 = "22.322"  # String (text)
print(f"num3 is of type: {type(num3)}")

num4 = '55.203'  # String (text)

print(f"num4 is of type: {type(num4)}")

# Mathematical operations on compatible data types

# Sum of num1 (float) and num2 (integer) - casting not required
print(f"The Sum of num1 and num2 is: {num1 + num2}")

# Sum of num2 (integer) and num3 (string) - conversion required
# We cannot directly add an integer and a string. Convert num3 to a float first.
print(f"The Sum of num2 and num3 (after converting num3 to float) is: {num2 + float(num3)}")

# Sum of num4 (string) and num3 (string) - not possible for mathematical operations
# Strings can be concatenated (joined), but not directly added for numerical operations.
# You'd need to convert them to numbers if intended for calculations.
# print(f"The Sum of num3 and num4 is: {num3 + num4}")  # This line is commented out

# Additional notes:
# - The comments explain the data types and conversion attempts.
# - Unintended lines causing errors are commented out for clarity.
# - You can explore converting strings to integers (int()) if they represent whole numbers without decimals.

