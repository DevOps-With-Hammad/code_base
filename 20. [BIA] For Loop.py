# 20. [BIA] For Loop
Deps = ["software engineering ", "DevOps", "Network", "Sys admins",
        "Backend ", "front_End", "Scrum Master", "Project manager "]
for x in Deps :
    print(x + " is a computer tech related object ")

for x in "YODA" :
    print(x + " This is the letters of the word YODA ")

Countries = ["software engineering ", "DevOps", "Network", "Sys admins",
             "Backend ", "front_End", "Scrum Master", "Project manager "]

for c in Countries :
    if c == "DevOps" or "Backend" :
        print(f"This is the related topics you've searched for {c}")
    else :
        print(c + " is  this filed are subjects related to tech industry\n "
                  "Do your best in that , you gonna thank me latter ")

Chart = ["Ahmed", "Ali", "Eslam", "Nagy", "Medhat", "Gamel", "Younis", "Alaa"]

for x in Chart :
    if x == "Nagy" :
        print(f"This is the Name you've searched for  {x}")
        break

    if x == "Alaa" :
        print(f"{x + Chart[0:9]} this is  ")