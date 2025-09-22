
n = 10

for i in range(1, n + 1):
    for y in range(n, i, -1):
        print(" ", end="")
    for x in range(1, i * 2):
        print("*", end="")
    print()

for i in range(n - 1, 0, -1):
    for y in range(n, i, -1):
        print(" ", end="")
    for x in range(1, i * 2):
        print("*", end="")
    print()