"""
initials.py - San Kwon
Initials More
This program prints a given name's initials.
"""

# ask for name and get rid of spaces in the front and back
name = input("")
name = name.strip()

# find initials
initials = ""
while name.find(" ") != -1:
    initials = initials + name[0].upper()
    space = name.find(" ")
    name = name[(space + 1):]
    while name[0] == " ":
        name = name[1:]
initials = initials + name[0] + "\n"

# print initials in uppercase
print(initials.upper())
