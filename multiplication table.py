# let's code

fnumber = 0
snumber = 1

while fnumber <= 13:
    if fnumber == 12:
        break
    fnumber =fnumber +1
    sum = snumber*fnumber
    print(f"{snumber}*{fnumber}={sum}")

# more than one table
# let's code

fnumber = 0
snumber = 1

while snumber <= 12 :  # Loop for different tables
    fnumber = 0  # Reset fnumber for each new table
    while fnumber <= 11 :
        fnumber += 1
        product = snumber * fnumber
        print(f"{snumber} * {fnumber} = {product}")

    print("\n")  # Adding a new line between tables for better readability
    snumber += 1  # Increment snumber to get the next table
