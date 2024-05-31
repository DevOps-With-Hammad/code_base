# 8. [BIA] Creating Basic Custom Functions Part 1
def your_name():
    your_name_dear = "Hamad"
    your_age = input(f"pls tell us your name mr : {your_name_dear}")
    math, arabic, english = 13, 24, 26

    print(f"{your_name_dear} , Hello and welcome ,"
          f"\n You should put your age \n "
          f"your max degrees is {max(math, arabic, english)}\n"
          f"your mini degrees is {min(math, arabic, english)} ")
your_name()
