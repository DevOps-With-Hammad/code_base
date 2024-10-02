# 12. [IGA] Exercise 4.4 Creating Basic Custom Functions Part 2
"""
1- Ask who was on Titanic?
2- What year is it currently?
3- print Jack and Rose was on Titanic which sink 112 ago

"""
passenger = input("Who was on titanic ?? ")
lauch_year = int(input("since when they lunch Titanic ??"))
def titanic(passenger, lauch_year):
    Year = 2024 - lauch_year
    print(f"{passenger} was on titanics \n "
          f"which sunk '{Year}' Years ago ")

titanic(passenger, lauch_year)