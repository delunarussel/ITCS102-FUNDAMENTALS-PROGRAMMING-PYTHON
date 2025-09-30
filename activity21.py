
isClean = True
while isClean == True:
    ask = input("Is the clothes clean already (yes/no)---> ")
    if ask.lower() == 'y':
        print("loop continue")
        continue
    else:
        print("loop stops")
        break
