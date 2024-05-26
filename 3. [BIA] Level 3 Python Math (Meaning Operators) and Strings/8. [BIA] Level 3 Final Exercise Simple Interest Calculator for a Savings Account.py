# Exercise:-
"""
You are an intern at a bank, and you've been tasked to create a simple program to calculate  the interest that
customers will earn on their saving account. The interest is calculated yearly using this formula
interest = (principle x rate x time ) / 100
"""
# Let's code :
# Instruction :-
# Create a variable named = Principle and assign the value of 1000 to it .(This is the initial amount in USD)
# Create a variable named = Rate and assign the value of 5 to it. (Annual interest rate in percentage)
# Create Variable named   = Time and assign the value of 2 to it. (Time in Years)
# Calculate the simple    = interest using the ##formula above. store the result in a variable named interest
# Print the interest amount rounded into 2 decimal places along with a message . This message should include
# (interest, rate, principle in it )

Principle = 1000
Rate = 5
Time = 2
Interest = (Principle * Rate * Time)/ 100
print(f"The Interest amount is :-\n {round(Interest)} \n"
      f" With a Principle value :- {Principle}"
      f",  Rate value = {Rate}"
      f", and Time value = {Time} ")

