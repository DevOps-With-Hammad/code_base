# 11. [BIGA] Using the MATCH and CASE Logic.

# importing platform
import platform
print(platform.python_version())

# Match case
army_size = input("Your aramy size here please \n ")
if army_size >= 10:
    print(f"This army \n the army  of {army_size} \n is a Jadi . \n wow you are doing great so far ")
elif army_size >= 100:
    print(f"This army \n The army size of {army_size}\n is a Yoda \n good Job  ")
elif army_size > 1000:
    print(f"This army \n The army size of {army_size} \n is considered as Bam army \n Wow ")
else:
    print(" You are so far beyond Options here\n Give it another Try please ")
