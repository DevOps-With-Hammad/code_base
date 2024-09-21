def is_power_of_two(number) :
    # Check for non-positive numbers
    if number <= 0 :
        return False

    # Divide number by 2 while it is greater than 1
    while number > 1 :
        # If the number is not divisible by 2, return False
        if number % 2 != 0 :
            return False
        number = number / 2

    # If the number becomes 1, it is a power of 2
    return number == 1


# Calls to the function
print(is_power_of_two(0))  # Should be False
print(is_power_of_two(1))  # Should be True
print(is_power_of_two(8))  # Should be True
print(is_power_of_two(9))  # Should be False
