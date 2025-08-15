amount = eval(input("Enter amount of deposit: "))

# Denominations
d1000 = 1000
d500 = 500
d200 = 200
d100 = 100
d50 = 50
d20 = 20
d10 = 10
d5 = 5
d1 = 1

# Calculations
thousands = amount // d1000
amount %= d1000

five_hundreds = amount // d500
amount %= d500

two_hundreds = amount // d200
amount %= d200

hundreds = amount // d100
amount %= d100

fifties = amount // d50
amount %= d50

twenties = amount // d20
amount %= d20

tens = amount // d10
amount %= d10

fives = amount // d5
amount %= d5

ones = amount // d1
amount %= d1

# Output
print("\nDenomination Breakdown:")
print("1000:", thousands)
print("500:", five_hundreds)
print("200:", two_hundreds)
print("100:", hundreds)
print("50:", fifties)
print("20s:", twenties)
print("10:", tens)
print("5:", fives)
print("1:", ones)