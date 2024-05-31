# 6. [BIA] Exercise 4.2 Input Built in Python Function
"""
Create a python code that ask for your name and age
Print it to the screen saying hi to that person

"""
name, age, dep = input("Hello dear,\n "
                       " please provide :- \n"
                       "your name: \n"
                       " age:\n"
                       " department:\n").split()
print(f"Welcome {name}\n  form {dep} ")