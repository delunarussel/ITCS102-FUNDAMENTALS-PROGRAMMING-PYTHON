from activity25_1 import *

name  = input("Whats is your name: ")

print(f"Welcome {name} to my File compiler")

t = True

while t == True:
    print("Select a program")
    print("A - Activity11\nB - Activity12\nC - Activity13\nD - Exit")

    new = input("What program would you like to run: ").lower()

    if new == "a":
        activity11()
        continue
    elif new == "b":
        activity12()
        continue
    elif new == "c":
        activity13()
        continue
    elif new == "d":
        print("exiting program...")
        break
    else:
        print("error input")
