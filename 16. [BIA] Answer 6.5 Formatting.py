# 16. [BIA] Answer 6.5 Formatting
"""
Rose will Purchase a 1st class ticket for 870 pounds
A 2nd class ticket (for baby Yoda )costs 100.42 pounds.
A 3rd class ticket (fo jack ) is 7 pound.

-Code this : How many 1st, 2nd 3rd class
 tickets do you want to purchase??
 Then print  this : the total   do you want to purchase?
  please use the formatting feature with 2 decimal points.
"""
print(" Welcome to the class ticket picker programme ")
tickets = input("Hello Mate\n"
                "Which class you want to pick here :- \n "
                "Choose among 1st, 2nd or 3rd \n ")
print(f" Good choice here Sir \n You've chosen {tickets}")
if tickets == "1st":
    price = 870
    print(f"Rose have purchased the ticket class{tickets}\n"
          f"Taking value {price} pound "
          f"Good Job Rose  ")
elif tickets == "2nd":
    price = 100.42
    print(f"Yoda have purchased the ticket class {tickets}\n"
          f"Taking value {price} pound"
          f"Good job Yoda ")
else:
    price = 7
    print(f"Jack have purchased the ticket class {tickets}\n "
          f"Talking value {price} pound "
          f"Good Job Jack all the best")

