def greeter(name):  
    print(f"Hello {name}, How are you? ")

def summ(x):   
    total = 0
    for y in range(x, 0, -1):
        total += y 
    print(f"The of {x} is {total}") 
greeter("russel")
greeter("marshall")
greeter("lee")
greeter("denji")


summ(15)
summ(3)
summ(9)
summ(18)