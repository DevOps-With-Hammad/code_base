# 5. [BIA] Floating and Boolean Data Types

num1 = 3.14  # Int
print(type(num1)) # you can use the print type method to identify the Vars (Num1, Num2, Num3, Num4) Data Types
num2 = 22  # float is an int value
print(type(num2)) # you can use the print type method to identify the Vars (Num1, Num2, Num3, Num4) Data Types
num3 = "22.322"  # Note  That is a str value
print(type(num3)) # you can use the print type method to identify the Vars (Num1, Num2, Num3, Num4) Data Types
num4 = '55.203'  # Note That is a Str value
print(type(num4)) # you can use the print type method to identify the Vars (Num1, Num2, Num3, Num4) Data Types

# let's try some math operation on that Vars

# first printout the sum of 2 Vars
print(f"The Sum of num1 and num2 is :>> {num1 + num2}")
# print(f"The Sum of num2 and num3 is :>> {num2 + int(num3)}")
        # you will get this error ValueError: invalid literal for int() with base 10: '22.322'

# output is The Sum of num2 and num3 is :>> 44.322
# print(f"The Sum of num2 and num3 is :>> {num4 + float(num3)}")
        # TypeError: can only concatenate str (not "float") to str
print(f"The Sum of num2 and num3 is :>> {float(num4) + float(num3)}")
        # The Sum of num2 and num3 is :>> 77.525
# print(f"The Sum of num2 and num3 is :>> {float(num4) + int(num3)}")
    # ValueError: invalid literal for int() with base 10: '22.322'
# print(f"The Sum of num2 and num3 is :>> {float(num4 + num3)}")
        # ValueError: could not convert string to float: '55.20322.322'

# print(f"The Sum of num3 and num4 is :>> {num3 + num4}")