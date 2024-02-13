print("Welcome to Robinsons Movie World")
print("----------------------------------------")
age = int(input("What is your age? "))
print("----------------------------------------")
if (age <= 12):
    print("The price is", 150)
elif (age <= 64):
    print("The price is", 250)
elif (age >= 65):
    print("The price is", 250 - 25)
else:
    print("Please input a correct age!")
