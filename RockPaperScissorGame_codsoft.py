import random

# Function to get user's choice
def get_user_choice():
    while True:
        print("Choose: Rock, Paper, or Scissors")
        user_choice = input().lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")

# Function to get computer's choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to play the game
def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Score - You: {user_score} | Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no)").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

# Start the game
play_game()