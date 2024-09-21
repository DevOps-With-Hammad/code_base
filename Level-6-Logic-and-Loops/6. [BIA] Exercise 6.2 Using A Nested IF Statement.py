# 6. [BIA] Exercise 6.2 Using A Nested IF Statement

"""
In this exercise we will create 2 if statement as follows :
-1 is the city belongs to african country .
-2 is the city african if yes ask if the city belongs to Egypt

"""
City = input("please input your city : ")
if City == "Cairo" or "ALex ":
    which_Country = input("Is your city belongs to Egypt ")
    if which_Country == "yes":
        print("welcome dear to the great ancient civilization of all time ")
    else:
        print("try again with a city form Egypt pls  ")

else:
    print(" you are far away form home dear \n give it a try later please ")