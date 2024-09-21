# 21. [BIA] Exercise 6.7 For Loop

"""
Create a for loop , that prints 2 lines as follows :
Leia I am your father
Luka I am your Father
"""
Call =["Leia I am your father ."
       ,"Luka I am your father."]

for x in Call :
    print(x +  f"{Call[0][-1]}" )