def value(number):
    sum = 0
    while number >=0:
        if number == 0 :
            break
        sum += number
        number = number - 1
    print(sum)

value(5)
value(3)
value(2)
