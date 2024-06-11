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
