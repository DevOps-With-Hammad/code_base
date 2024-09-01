# for Loop
Deps = {"Animals":["cat", "Dog", "Cow"],
         "Birds":["duck", "sparrow", "ravin"],
        "Colors":["greeen", "yellow", "White"]
}
print(Deps["Animals"])
print(Deps["Animals"][:2])
print(Deps["Animals"][0:2])
print(Deps["Animals"][:-2])

print(Deps["Birds"][:3], "\n",
      Deps["Birds"][0:3], "\n",
      Deps["Colors"][0:2]
      )

for x in Deps:
    if Deps["Colors"][1] == "yellow":
        print(f"This is the second element in the the Dec Deps which is : \n "
          f"{Deps["Colors"][1]}")