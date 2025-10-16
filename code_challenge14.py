# odd number compiler
name = input("Hi, What is your name? --->")

print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
print("ODD number compiler, enter '0' to terminate loop")

sum = 0
odd = ""
tuloy = True

while tuloy:
    numb = eval(input("Enter a number--->"))
    if numb % 2 == 1:
        print ("Odd number detected")
        odd += str(numb) + ","
        sum += numb
        continue
    elif numb == 0:
        print("Terminating loop...")
        break
    else:
        if numb % 2 == 0:
            print("Even number, skipping...")
        else:
            print("Invalid input")
        continue
print(f"Hi {name}, The sum of all ODD number is {sum}")
print(f"All the ODD numbers you input is {odd}")