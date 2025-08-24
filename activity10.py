#comments
#jeepney fare #user would input their name
#if user is student student discount must be applied
#20% discount on student, if not student no discount

name = input("Input your name ---> ")
isStudent = input("Are you a student (Yes / No) --> ")
fare = float(input("Bayad --> "))

if isStudent.lower() == "yes":
    discount = fare * 0.20
    new_fare = fare - discount
    print("Hi", name + ", your student discount is", discount,
          "and your discounted fare is", new_fare)
else:
    print("Sorry", name + ", you are not eligible for a discount.")