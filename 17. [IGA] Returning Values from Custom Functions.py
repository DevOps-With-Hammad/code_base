# 17. [IGA] Returning Values from Custom Functions
aa = int(input("Pls input the temps in digits \n"))


def converter(aa):
    clss = (aa - 32) / 1.8
    print(f"Here is your converted data of the current temps that you've input :\n {clss}")


converter(aa)


def converter2(a):
    return (a - 32)/1.8
print((converter2(80)))


def converter2(a1):
    return (a1 - 32)/1.8

converter2(int(a = 80))

