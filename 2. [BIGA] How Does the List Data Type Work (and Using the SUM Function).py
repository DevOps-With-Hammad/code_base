# 2. [BIGA] How Does the List Data Type Work (and Using the SUM Function)
Hammad_experience = 12
Sbaah_experience = 24
total_experience = [Hammad_experience, Sbaah_experience]
print(f"The total Experience is {sum(total_experience)}")

#let's try a previous lesson from Level4 with this new way.
val1 = float(input("Welocme to calculator app dear! \n "
                   "what is your first value = \n"))
sign = input("and your operator is (/, *, - or + \n ")
val2 = float(input("WHat is your other value = \n "))


def add(a, b) :
    return a + b


def subtract(a, b) :
    return a - b


def division(a, b) :
    return a / b


def multiplication(a, b) :
    return a * b


def operaiton(a, b, ops) :
    if ops == "+" :
        return add(a,b)
    elif ops == "-" :
        return subtract(a,b)
    elif ops == "*" :
        return multiplication(a,b)
    elif ops == "/" :
        return division(a,b)
    else :
        return "pls insert a valid operator.\n try again next time"


result = operaiton(val1, val2, sign)
print(f"the final result is = {result}")
