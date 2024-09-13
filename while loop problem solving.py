def sum_of_integers(n):
    if n < 1:
        return 0

    i = 1  # Start from 1
    sum = 0  # Initialize the sum

    while i <= n:  # Loop until i reaches n
        sum += i  # Add i to total_sum
        i += 1  # Increment i by 1

    return sum  # Return the total sum


# Test cases
print(sum_of_integers(3))  # should print 6
print(sum_of_integers(4))  # should print 10
print(sum_of_integers(5))  # should print 15