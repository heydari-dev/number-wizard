import random

# Get user's name
name = input("Welcome! What's your name? ")

# Get user's chosen number and validate input
while True:
    try:
        number = int(input("Please select a number between 0 and 100: "))
        if 0 <= number <= 100:
            break
        else:
            print("The number must be between 0 and 100.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Initializing the random chance value
chance = random.randint(0, 100)

# Guessing loop
while number != chance:
    print(f"My guess is: {chance}")
    hint = input("Is your number higher or lower? (Type 'up' for higher, 'down' for lower): ").strip().lower()

    if hint == "up":
        if chance < 100:
            chance = random.randint(chance + 1, 100)
        else:
            print("The guess is already at the maximum value (100). Please check your input.")
    elif hint == "down":
        if chance > 0:
            chance = random.randint(0, chance - 1)
        else:
            print("The guess is already at the minimum value (0). Please check your input.")
    else:
        print("Invalid input! Please type 'up' or 'down'.")

# End of the game
print(f"Victory! The number is {chance}. Congratulations, {name}!")
