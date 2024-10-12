import random

# Function to get the computer's choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif user_choice == "rock" and computer_choice == "scissors":
        return 'user'
    elif user_choice == 'scissors' and computer_choice == 'paper':
        return 'user'
    elif user_choice == 'paper' and computer_choice == 'rock':
        return 'user'
    else:
        return 'computer'

# Function to display the result
def get_user_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("You win!")
    else:
        print("You lose!")

# Main game function
def play_game():
    computer_score = 0
    user_score = 0
    play_again = 'yes'

    # Continue playing until the user enters 'no'
    while play_again.lower() == 'yes':
        print("\nLet's play Rock, Paper, Scissors!")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

        # Keep prompting until a valid input is given
        while user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")
            user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

        # Get computer's choice and determine the winner
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        get_user_result(user_choice, computer_choice, winner)

        # Update scores based on the winner
        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1

        print(f"\nCurrent Score: You - {user_score}, Computer - {computer_score}")

        # Ask the user if they want to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()

        # Ensure valid input for the 'play again' option
        while play_again not in ['yes', 'no']:
            print("Invalid option! Please enter 'yes' or 'no'.")
            play_again = input("Do you want to play again? (yes/no): ").lower()

    print(f"\nFinal Score: You - {user_score}, Computer - {computer_score}")
    print("Thanks for playing!")

# Start the game
if __name__ == "__main__":
    play_game()
