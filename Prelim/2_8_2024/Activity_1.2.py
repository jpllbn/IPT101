age = int(input("Enter your Age: "))
member = input("Are your a member? (Yes/No): ")


if age >= 60:
    if member == "Yes":
        print("Your are Qualify for a Senior Discount.")
    else:
        print("Consider joining our program for even more benefits!")
elif age >= 18:
    if member == "Yes":
        print("You are Qualify for a Standard Pricing.")
    else:
        print("Consider joining our program for even more benefits!")
else:
    print("You are not eligible for any discount at this time.")