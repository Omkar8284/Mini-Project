import random

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)
guess_count = 0
user_guess = 0

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. Can you guess it?")

# Loop until the user guesses the correct number
while user_guess != number_to_guess:
    try:
        user_guess = int(input("Enter your guess: "))
        guess_count += 1
        
        if user_guess > number_to_guess:
            print("Lower number please.")
        elif user_guess < number_to_guess:
            print("Higher number please.")
        else:
            print(f"Congratulations! You guessed the number in {guess_count} tries.")
    except ValueError:
        print("Please enter a valid integer.")
