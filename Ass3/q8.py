import random

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input("Enter your choice: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_wins = 0
    computer_wins = 0

    for round in range(1, 6):
        print(f"\nRound {round}:")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose {user_choice}.")
        print(f"Computer chose {computer_choice}.")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "you" in result.lower():
            user_wins += 1
        elif "computer" in result.lower():
            computer_wins += 1

    print(f"You won {user_wins} rounds.")
    print(f"Computer won {computer_wins} rounds.")

    if user_wins > computer_wins:
        print("Congratulations! You are the overall winner!")
    elif user_wins < computer_wins:
        print("Game Over!, the computer is the overall winner!")
    else:
        print("It's a tie!")

# Start the game
play_game()
