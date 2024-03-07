celsius = int(input("Enter Celsius: "))
f = (celsius*9/5)+32

if f <= 0:
    print("Fahrenheit: ", f)
    print("Wow it is cold today")
elif f <= 32:
    print("Fahrenheit: ", f)
    print("It is freezing today")
elif f <= 50:
    print("Fahrenheit: ", f)
    print("It is chilly today")
elif f <= 80:
    print("Fahrenheit: ", f)
    print("It is nice outside today")
else:
    print("Fahrenheit: ", f)
    print("It is really hot today")



