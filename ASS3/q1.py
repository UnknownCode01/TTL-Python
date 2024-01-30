import random
import re

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except:
        return None

def main():
    print("Guess the nummber between 1 to 5 game ")
    secret_number = random.randint(1,5)
    player_guess_expression = input("Your guess (may be expression format): ")
    # Check if the input is a valid expression
    if re.match(r'^[1-5+\-*/()\s]+$', player_guess_expression):
        # Evaluate the expression
        player_guess = evaluate_expression(player_guess_expression)
        if player_guess is not None:
            if player_guess == secret_number:
                print("Congratulations! You guessed the correct number.")
            else:
                print(f'Incorrect guess, correct -> {secret_number}')
        else:
            print("Invalid expression. Please enter a valid mathematical expression.")
    else:
        print("Invalid input. Please enter a valid expression using numbers 1 to 5 and basic operators (+, -, *, /).")

if __name__ == "__main__":
    main()
