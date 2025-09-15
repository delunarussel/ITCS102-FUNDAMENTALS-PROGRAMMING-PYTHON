# Enter 10 numbers, determine if odd or even, and find the summation of odd numbers

total = 0

for me in range(1, 11):   
    num = int(input("Enter number ---> "))

    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")
        total += num   

print("\nThe sum of all odd numbers entered is:", total)

   