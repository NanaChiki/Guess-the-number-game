import random, time

def play_again(game_over):
    if game_over:
        print("Game Over! Try again next time!")

    while True:
        play_again = input("Do you want to play again? (Yes/No): ").strip().capitalize()
        if play_again in ["Yes", "No"]:
            break
        print("Invalid input! Please enter 'Yes' or 'No'.")
        
    if play_again != "Yes":
        print("Thanks for playing! Goodbye!")
    return play_again == "Yes"

def end_game(random_number):
    print("No attempts remaining.")
    time.sleep(2)
    print(f"The number was {random_number}.")
    time.sleep(2)
    return play_again(True)

def check_values():
    while True:
        try:
            min_value = int(input("Minimum value: "))
            max_value = int(input("Maximum value: "))
            if min_value < max_value:
                return min_value, max_value
            print("Invalid input! Minimum value must be less than maximum value.")
        except ValueError:
            print("Invalid input! Please enter int values.")

def get_guess_number(min_value, max_value):
    while True:
        try:
            guess = int(input(f"Guess the number between {min_value} and {max_value}: ").strip())
            return guess
        except ValueError:
            print("Invalid input! Please enter an integer value.")

def play_game():
    play = True
    while play:
        print("Welcome to the Guessing Game!")
        print("You have 5 attempts to guess the number.")
        print("Enter the minimum and maximum values for the guessing game!!!")
        min_value, max_value = check_values()
        random_number = random.randint(min_value, max_value)
        left_attempts = 5

        while left_attempts > 0:
            print(f"Attempts left: {left_attempts}" if left_attempts > 1 else "You have the last attempt left.")
            guess_number = get_guess_number(min_value, max_value)
            print("Processing your guess...")
            time.sleep(2)

            if guess_number == random_number:
                attempt_number = 5 - left_attempts + 1
                print(f'Congratulations! You nailed it at the {attempt_number} {"attempt" if attempt_number == 1 else "attempts"}.')
                if not play_again(False):
                    play = False
                break
            elif left_attempts == 1:
                if not end_game(random_number):
                    play = False
                break
            elif guess_number < random_number:
                print("The number is higher than your guess.")
            else:
                print("The number is lower than your guess.")

            left_attempts -= 1
            
play_game()


    




