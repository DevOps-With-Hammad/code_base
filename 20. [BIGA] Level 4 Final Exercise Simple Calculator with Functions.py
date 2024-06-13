# 20. [BIGA] Level 4 Final Exercise Simple Calculator with Functions


print("Hello to the Calculator App")
num1 = int(input("Pls input your First  number :-\n"))
num2 = int(input("Pls input your second  number :-\n"))
sign = input("which operation sign you want to add \n"
             " /, *, - or + \n ")


# define the add function
def add() :
    answer = num1 + num2
    # return (f"total value is = {answer}")
    print(f"total value is = {answer}")


add()


# define the subtract function
def subtract() :
    answer = num1 - num2
    return f" the final answer is = {answer}"


print(subtract())


# define the multiple function
def multiple() :
    answer = num1 * num2
    return f" the final answer is = {answer}"


print(multiple())


# define the Divide function
def divide() :
    answer = num1 / num2
    return f" the final answer is = {answer}"


print(multiple())


# define the Divide function
def signs() :
    if sign == "+" :
        add()
    elif sign == "-" :
        subtract()
    elif sign == "*" :
        multiple()
    elif sign == "/" :
        divide()
    else :
        return "Pls insert a valid sign ( /, *, -, +) \n try again "


(signs())
