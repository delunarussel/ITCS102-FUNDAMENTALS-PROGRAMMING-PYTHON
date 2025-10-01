
#diamond pattern
for i in range(1,4,1):
    for y in range(1,4,1):
        print(" ",end=" ")
    for x in range(3,i,-1):
        print(" ",end=" ")
    for z in range(1,i,1):
        print("*",end=" ")
    for w in range(0,i,1):
        print("*",end=" ")
    print()
#diamond pattern
for i in range(1,4,1):
    for y in range(1,4,1):
        print(" ",end=" ")
    for x in range(0,i,1):
        print(" ",end=" ")
    for z in range(2,i,-1):
        print("*",end=" ")        
    for w in range(3,i,-1):
        print("*",end=" ")
    print()


#triangle pattern
for i in range(1,7,1):
    for y in range(6, i, -1):
        print(" ",end=" ")
    for x in range(1, i, 1):
        print("*",end=" ")
    for x in range(0, i, 1):
        print("*",end=" ")
    print()
for i in range(1,7,1):
    for y in range(6, i, -1):
        print(" ",end=" ")
    for x in range(1, i, 1):
        print("*",end=" ")
    for x in range(0, i, 1):
        print("*",end=" ")
    print()
for i in range(1,7,1):
    for y in range(6, i, -1):
        print(" ",end=" ")
    for x in range(1, i, 1):
        print("*",end=" ")
    for x in range(0, i, 1):
        print("*",end=" ")
    print()
#trunk
for i in range (1,4,1):
    for y in range(1,5, 1):
        print(" ",end=" ")
    for x in range(1, 4, 1):
        print("*",end=" ")    
    print()



