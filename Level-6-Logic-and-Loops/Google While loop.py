def is_power_of_two(number):
    if number == 0:
        print(f"The Value is False (0 is not a power of two)")
        return False
    while number % 2 == 0:
        number = number / 2

    if number == 1:
        print(f"The Value is True ")
        return True
    print(f"The Value is False ")
    return False

is_power_of_two(9)
is_power_of_two(8)
is_power_of_two(7)
is_power_of_two(6)
is_power_of_two(5)
is_power_of_two(4)
is_power_of_two(3)
is_power_of_two(2)
is_power_of_two(1)
is_power_of_two(0)
