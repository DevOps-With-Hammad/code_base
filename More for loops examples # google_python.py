num = 1
for n in range(1,10):
    num = (num *n)
print(num)
""""""

def to_cel(x):
    return (x-32)*5/9
for x in range(0,101,10):
    print(x,to_cel(x))