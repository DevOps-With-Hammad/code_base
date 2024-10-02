# 11. [IGA] Creating Basic Custom Functions Part2
Name = input("what is your name ?")
age = str(input(f"what is your age Mr{Name}"))

def user(Name, age):
    age_next_year = int(age)+1
    print(f"Hello Mr :{Name}\n"
          f"In one year form now your age will be {age_next_year} ")

user(Name, age)

