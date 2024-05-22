# 11. [BIA] Level 2 Final Exercise Currency Converter
User_CUrr = input("Hello to The US to ERU Currency Converter  "
                  "\n Pls type which your prefer to convert to "
                  "\nUS or ERU: \n ")

if User_CUrr == "US":

    Val_To_Eru = input("your value in ERU here pls : \n ")
    print(f" Here is your ERUs to into US Dollar : \n {float(Val_To_Eru) * float(1.08)}")

elif User_CUrr == "ERU":
    Val_To_US = input("your value in ERU here pls : \n ")
    print(f" Here is your ERUs to into US Dollar : \n {float(Val_To_US) * float(0.92)}")
else:
    print("Pls input A valid Value")