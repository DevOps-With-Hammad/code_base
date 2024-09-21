# 15. [BIA] Exercise 6.5 Formatting
"""
Rose will Purchase a 1st class ticket for 870 pounds
A 2nd class ticket (for baby Yoda )costs 100.42 pounds.
A 3rd class ticket (fo jack ) is 7 pound.

-Code this : How many 1st, 2nd 3rd class
 tickets do you want to purchase??
 Then print  this : the total   do you want to purchase?
  please use the formatting feature with 2 decimal points.
"""
tickets = input("Please choose what class you need"
                " here of the current tickets"
                "1st, 2nd or 3rd ")

if tickets == "1":
    price = 870

elif tickets == "2":
    price =100.42
else:
    price = 7


print(f"The selected mount is {price}")