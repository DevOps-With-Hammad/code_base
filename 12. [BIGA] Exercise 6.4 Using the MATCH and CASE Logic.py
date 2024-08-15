# 12. [BIGA] Exercise 6.4 Using the MATCH and CASE Logic
# Ask the user to inter 1, 2 or 3 for the team
# Then use the match case logic to print :-
# your selected team 1
# your selected team 2
# your selected team 3

# Let's code :-

Team_selection = input("Please enter your selected team form 1 ,2 or 3 ")
match Team_selection:
    case "1":
        print("You have selected the team 1 ")
    case "2":
        print(" You have selected the team 2 ")
    case "3":
        print("You have selected  the Team  3 ")

