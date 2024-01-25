# Python Variables
# Variables are containers for storing data values
# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.
# Variables do not need to be declared

# A variable can have a short name (like x and y) or a more descriptive name (age, carnmae, total_volume)
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z), (0-9)
from colorama import *
import pyfiglet

banner = pyfiglet.figlet_format("January 25", font="doom")
print(Fore.RED + banner)

print(Fore.LIGHTCYAN_EX)
print("Twinkle, twinkle, little star, \nHow I wonder what you are! \nUp above the world so high, \nLike a diamond in the sky. \nTwinkle, twinkle, little star, How I wonder what you are!")

print(Fore.LIGHTGREEN_EX)
x = 5
y = "John"
print(x)
print(y)

# If you want to specify the data type of a variable, this can be done with casting
x = str("Name")
y = int(3)
z = float(3.0)
print(x)
print(y)
print(z)

# Built in Functions
# type() - use to check the hold data is correct


# Assign Multiple Values

# 1.Many Values to Multiple Variables:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Note: Make sure the number of variables matches the number of values, or else you will get an error.

# 2.One Value to Multiple Variables:

x = y = z = "Orange"
print(x)
print(y)
print(z)

# 3.Unpack a Collection

fruits = ["Apple", "Banana", "Cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables

# print() Function
# You can also use the + operator to output multiple variables:
# For numbers, the + character works as a mathematical operator

x = "Python"
y = "is"
z = "awesome"
print(x, y,  z)

# In the print() function, when you try to combine a string and a number with the + operator:
x = 5
y = "John"
print(x,y)

# Exercise
a = "My age is"
b = 21
print(a,b)

# Global Variables
# Variable that are created outside of a function are known as global variables
# Global variables can be used by everyone, both inside of functions and outside.

# Take Note: All function() followed by a paranthesis () called a function

x = "awesome"
def myfunc():
    global x
    x = "fanstastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

# The global keyword
#







