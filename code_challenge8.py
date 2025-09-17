print("hello world")
#Ask the user to input a number.Use a for loop to print the multiplication table from for that number.
# Format each line clearly (e.g., 5 x 1 = 5).

print("MULTIPLICATION TABLE MAKER")
numb =  eval(input("Input a number --> "))
print("Multiplication table for:", numb)
for me in range(1, 11):
    print(numb, "x", me, "=", numb * me)
