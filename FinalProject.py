def Armish():
    print("\n--- SMART CALCULATOR ---")
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    if op == '+':
        print("Result:", num1 + num2)
    elif op == '-':
        print("Result:", num1 - num2)
    elif op == '*':
        print("Result:", num1 * num2)
    elif op == '/':
        print("Result:", num1 / num2)
    else:
        print("Invalid operator")

def GuessGame():
    import random

    play_again = "yes"

    while play_again == "yes":

        secret_number = random.randint(1, 50)
        attempts = 0

        print("I have selected a number between 1 and 50. Try to guess it!")

        guess = 0
        while guess != secret_number:
            guess = int(input("Enter your guess: "))
            attempts = attempts + 1

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print("Correct! You guessed the number in", attempts, "attempts.")

        play_again = input("Do you want to play again? (yes/no): ").lower()

    print("Thanks for playing!")