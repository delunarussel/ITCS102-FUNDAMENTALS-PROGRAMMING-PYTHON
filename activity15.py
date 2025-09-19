 #STRING FORMATTING
#firstname = 'leonard'
# mid_name = 'andrew'
# Iname = 'mesi
#print("My name is ", firstname," ", mid_name," ", lname)
#print(f"My name is {firstname.upper()} {mid_name.upper()) {1name.upp
#input 10 numbers, get the summation of all the odd numbers

odd_sum = 0
for i in range(1,11,1):
    num = eval(input(f"{i} Enter a number --> "))
    if num % 2 == 1:
        odd_sum += num
print(f"The sum of all the ODD numbers given is {odd_sum}")