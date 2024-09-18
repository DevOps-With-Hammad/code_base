def count_to_ten():
  # Loop through the numbers from first to last
  x = 1
  while x <= 10:
    print(x)
    x += 1


count_to_ten()

#######################
def sequence(low, high) :
  # Outer loop to run twice
  for x in range(2) :  # Runs twice to create two rows
    # Inner loop to print from 'high' to 'low'
    for y in range(high, low - 1, -1) :  # Decrementing from 'high' to 'low'
      if y == low :
        # Don’t print a comma after the last item
        print(str(y))
      else :
        # Print a comma and a space between numbers
        print(str(y), end=", ")
    # Print a newline after each row
    print()


sequence(1, 3)


#############################
def odd_numbers(maximum) :
  return_string = ""  # Initializes variable as a string

  # Complete the for loop with a range that includes all
  # odd numbers up to and including the "maximum" value.
  for x in range(maximum + 1) :
    # Complete the body of the loop by appending the odd number
    # followed by a space to the "return_string" variable.
    if x % 2 != 0 :
      print(x, end=" ")

  # This .strip command will remove the final " " space
  # at the end of the "return_string".
  return return_string.strip()


print(odd_numbers(6))  # Should be 1 3 5
print(odd_numbers(10))  # Should be 1 3 5 7 9
print(odd_numbers(1))  # Should be 1
print(odd_numbers(3))  # Should be 1 3
print(odd_numbers(0))  # No numbers displayed

#########
x = 1
sum = 0
while x <= 10:
    sum += x
    x = x+1
print(sum)

