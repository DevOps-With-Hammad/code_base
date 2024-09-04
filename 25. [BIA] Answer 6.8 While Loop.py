# 25. [BIA] Answer 6.8 While Loop
"""
Create  a while loop print this :-

1 the year is 1901 >> This is the year when nobody found Titanic yet .
1 the year is 1902 >> This is the year when nobody found Titanic yet .
1 the year is 1903 >> This is the year when nobody found Titanic yet .

The year is 1984 when titanic found.
"""

Year = 1901
while Year <= 1984:
    if Year < 1984:
        print(f"The year is {Year} . Not the year when they found titanic ")
    else:
        print(f"WOW\n {Year} \n This is the year where they found titanic \n good work ")

    Year = Year + 1
