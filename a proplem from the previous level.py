# simple calculator aap
print("Hello TO the Calculator App.")
val1 = float(input("your first number is = : "
                   "\n "))
operatorz = input("Pls pick an operator :"
                  "\n ('/' , '*' , '-' , '+'"
                  "\n ")
val2 = float(input("your first number is = : "
                   "\n "))


def add(a, b) :
    return a + b


def subtrat(a, b) :
    return a - b


def divide(a, b) :
    return a / b


def multiply(a, b) :
    return a * b


def operation(a, b, operatorz) :
    if operatorz == "*" :
        return multiply(a, b)
    elif operatorz == "/" :
        return divide(a, b)
    elif operatorz == "-" :
        return subtrat(a, b)
    elif operatorz == "+" :
        return add(a, b)
    else :
        return "pls insert a vaild operator "


result = operation(val1, val2, operatorz)
print(f"The final result is : \n"
      f"{result}")
