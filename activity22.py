import random



num = random.randint(1,10)

tries = 0
r = True

while r == True:
    g = int(input("What number u guess(1-10): "))
    tries += 1

    if g == num:
        print("Congratulation")
        print(f"the number is {num}")
        print(f"YOu online took {tries} tries")
        break

    else:
        print("incorrect")
        continue
 