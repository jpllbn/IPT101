gender = input("What is your gender (male/female)? ")
age = int(input("What is your age? "))
citizen = input("Are you a citizen? ")
record = input("You have a criminal  record? ")

male = gender=="male" and age >=18 and citizen=="yes" and record=="no"
female = gender=="female" and age >=18 and citizen=="yes" and record=="no"

if (male or female):
    print("You are qualified")
else:
    print("You are not qualifed")
