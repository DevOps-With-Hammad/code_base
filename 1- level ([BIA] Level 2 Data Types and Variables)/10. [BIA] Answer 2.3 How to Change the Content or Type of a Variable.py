# 10. [BIA] Answer 2.3 How to Change the Content or Type of Variable
Height = str("1.09")
Height0 = "2.09"
Height1 = '3.09'
print(Height)
# 1.09
print(Height0 + Height1)
# 2.093.09

# print(float(Height0) + Height1)
# TypeError: unsupported operand type(s) for +: 'float' and 'str'
# print(float(Height0 + Height1))
# ValueError: could not convert string to float: '2.093.09'
# print(float(Height0) + int(Height1))
# ValueError: invalid literal for int() with base 10: '3.09'
print(float(Height0) + float(Height1))
# 5.18
# print(int(Height0) + float(Height1))
# ValueError: invalid literal for int() with base 10: '2.09'
if Height0.isdigit() :
    Height00 = float(Height0)
    print(Height00 + float(Height1))
else :
    print("Try to look at the code again ")

print((float(Height1)) + float(Height0))
# 5.18
print(int(float(Height1)) + float(Height0))
# 5.09
print(int(float(Height1) + float(Height0)))
# 5

# print(float(int(Height1) + int(Height0)))
# ValueError: invalid literal for int() with base 10: '3.09'
