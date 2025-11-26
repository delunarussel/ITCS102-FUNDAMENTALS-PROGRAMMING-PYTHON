print("welcome to the dictionary")
print("========================================")

tuloy = True

empty_dictionary = {}
def print_anime():
    for i,j in empty_dictionary.items():
        print(f"code {i}, anime -- {j}")
def pang_search(key):
    print("searching......")
    print(f"result shows {empty_dictionary[key]} onour database")

while tuloy == True:
    keys = input("input keys for this anime ----->>>")

    value = input("enter an anime title ------  >>>>")

    empty_dictionary[keys] = value

    choice = input("would you like to continue adding anime \ny -YES\nn -NO\np -PRINT ").lower()

    if choice =='y':
        print("continuing...")
        continue
    elif choice =='n':
        print("program stops")
        break
    elif choice == 'p':
        print_anime()
        continue
    else:
        print("inavalid input")


