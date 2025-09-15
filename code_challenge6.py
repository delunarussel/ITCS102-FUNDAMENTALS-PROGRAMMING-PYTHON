#Factoriral Program

print("factorial Program")


num = eval(input("Enter a number"))


result = 1
for me in range(num, 0, -1):
    result *= me
    #print(result)

print("The Factorial of", str(num) +" is", result)