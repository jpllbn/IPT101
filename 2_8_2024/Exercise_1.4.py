user = int(input("What is your age? "))

legalage = 18
if user >= legalage:
    print("Legal Age")
    gender = input("Are you Male or Female: ")
    if gender == "Male":
        print("Drink Alcohol")
    else:
        print("Go to Sleep")
else:
    print("You are not in Legal age")