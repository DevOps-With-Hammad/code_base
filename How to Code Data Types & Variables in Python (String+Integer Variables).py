# How to Code Data Types & Variables in Python (String+Integer Variables\


# String Part >>>>
print("Hello world ")
print('Hello world ')

# print(str"Hello world ")
"""
SyntaxError: invalid syntax
"""
# Vars In python
name = 'hammad'
name1 = "hammad"
# name3 = str'hammad'
"""
SyntaxError: invalid syntax
"""
#  name4 = str"hammad"
"""
SyntaxError: invalid syntax
"""

name5 = str("hammad ")
# name6 = str(hamamd)
"""
SyntaxError: invalid syntax
"""
name7 = str('Hammad')
print(name7)

# Integer Part >>
print(12)
print("12")  # this one you can't operate a math on it
print('12')  # That too can't operate to it a math operation

# Let's put that into Vars  as you can see :-
var1 = 12
var2 = "12"  # this one you can't operate a math on it
var3 = '12'  # That too can't operate to it a math operation
# Let's printout the result
print(var1)  # also we can add some magic by implementing text to the out put
print(f"This is th out put of Var1>>   {var1}")
# but if you gonna to print the other Var2 nd Var3 you will get it printed  as you can see but syntax error when
# performing a math operation to it .

print(f"here is the output of Var 2:>>  {var2} \n Also Var3 is gonna be :>> {var3}")
# let's put these Var2 and Var3 into Math operation
# print(f" Here is the sum of Var2 and VAr 3 : >> {var2 + var3}\n  Also var1 + var2 :>> {var1 + var2}")
"""
TypeError: unsupported operand type(s) for +: 'int' and 'str' 
Here what you will get .. How to FIx that 
you got 2 ways here . use the convert method to int or to change the var from str to int
let's give it a try .
"""
print(f" Here is the sum of Var2 and VAr 3 : >> {int(var2) + int(var3)}\n  Also var1 + var2 :>> {var1 + (int(var2))}")
print(f" Here is the sum of Var2 and VAr 3 : >> {int(var2 + var3)}\n  Also var1 + var2 :>> {var1 + int(var2)}")



