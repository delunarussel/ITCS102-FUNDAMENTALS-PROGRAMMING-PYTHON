

anime = True
akagi = []
while anime == True:
    title = input("Enter the title of an anime you like (or type 'done' if you are finish): ")
    if title.lower() == 'done':
        print("you have exited the anime entry program.")
        print("this is your updated list of anime:")
        for i in akagi:
            print("*", i)
        break
    else:
        akagi.append(title)
        print(f"'{title}' has been added to your anime list:")
        continue