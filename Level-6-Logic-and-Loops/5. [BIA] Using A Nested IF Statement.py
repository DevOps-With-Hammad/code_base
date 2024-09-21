# 5. [BIA] Using A Nested IF Statement
Jedi_test = input("Is the charachter holiding a lightsaber??")
if Jedi_test == "yes":
    print("The character is Jedi ")
    cha_color = input(" what is the Jedi character color?i  ")
    if cha_color == "red" or "green" or "blue":
        print(f"this is a Jedi char colored by {cha_color}")
else:
    print(" I think you have no current choice here active ")