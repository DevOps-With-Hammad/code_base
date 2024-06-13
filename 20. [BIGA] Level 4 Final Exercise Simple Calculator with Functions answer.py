print("Hello to the Calculator App")
num1 = int(input("Pls input your first number :-\n"))
num2 = int(input("Pls input your second number :-\n"))
sign = input("which operation sign you want to add \n /, *, - or + \n ")


# define the add function
def add(a, b):
    return a + b


# define the subtract function
def subtract(a, b):
    return a - b


# define the multiply function
def multiply(a, b):
    return a * b


# define the divide function
def divide(a, b):
    return a / b


# define the signs function
def signs(a, b, operation):
    if operation == "+":
        return add(a, b)
    elif operation == "-":
        return subtract(a, b)
    elif operation == "*":
        return multiply(a, b)
    elif operation == "/":
        return divide(a, b)
    else:
        return "Pls insert a valid sign ( /, *, -, +) \n try again "


# Get the result from signs function
result = signs(num1, num2, sign)

# Print the result
print(f"The final answer is = {result}")
