secret_value = 28
total = 0

print("WELCOME TO THE GUESSING GAME!")
print("Try to guess the secret number between 1  and 100")

user = int(input(f"\nEnter your guess (or 0 to quit): "))

while user != 0:

    if user == 0:
        print("Quitting the game. Thanks for playing!")

    if user == secret_value:
        total += 1
        print(f"Congratulations! You guessed the secret number {secret_value}")
        print(f"It took you {total} attempts to guess the number.")
        break

    if user < secret_value:
        print("Too low! Try again.")
        total += 1
        user = int(input(f"\nEnter your guess (or 0 to quit): "))
    elif user > secret_value:
        print("Too high! Try again.")
        total += 1
        user = int(input(f"\nEnter your guess (or 0 to quit): "))
