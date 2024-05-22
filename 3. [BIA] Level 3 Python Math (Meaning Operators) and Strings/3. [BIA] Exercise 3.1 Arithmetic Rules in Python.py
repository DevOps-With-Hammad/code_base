# 3. [BIA] Exercise 3.1 Arithmetic Rules in Python

print("hello world")

yga = 12
yga0 = 12.0203
yga1 = "3.014"
yga2 = '3.156'
yga3 = 15 / 16
# sum = yga + yga0 + yga1 + yga2 + yga3
# print(sum)
# TypeError: unsupported operand type(s) for +: 'float' and 'str'
#sum = yga + yga0 + float(yga1) + yga2 + yga3
#print(sum)
#TypeError: unsupported operand type(s) for +: 'float' and 'str'

um = yga + yga0 + float(yga1) + float(yga2) + yga3
print(um)
aveg = um / 5
print(aveg)