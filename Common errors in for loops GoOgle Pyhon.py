# Common errors in for loops
"""
for x in 25: # should put the Range function
     print(x )
"""

for x in range(25):
    print(x)
    # This will make the error go away

def greeting(frends):
    for frend in frends:
        print(f"Hi , {frend}")

greeting(["ali", "abdo", "mazen", "kamel"])