# 15. [IGA] Exercise 4.5 Creating Advanced Functions  Keyword and Default Values)
"""
Create a function my_age with one variable in brackets called age
In the custom function, print my age is [your age .
Call the function using the age 39
change the default age to 19
call the function with nothing in bracket

"""
def my_age(age):
    print(f"myage is {age}")
    age = input("what is your age")
    print(f"my age is {age}")

my_age(39)
my_age(19)