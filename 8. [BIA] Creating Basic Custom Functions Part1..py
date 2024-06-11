def home():
    name = input("What is your name, dear: ")
    department = input("What is your department: ")

    if not name:
        print("It is the right value for the right record.")
    elif department.isdigit():
        print("Now you're doing great with numbers.")
    else:
        print("Oh no, you should do more practice.")

home()
"""
This is a function  takes 2 parameters as name and number of department. then checks if the inserted value are the right
 value for this records.
 return a message about the status value.
"""