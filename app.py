import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (
        (player_choice == 'rock' and computer_choice == 'scissors') or
        (player_choice == 'paper' and computer_choice == 'rock') or
        (player_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "win"
    else:
        return "lose"

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    wins = 0
    losses = 0
    ties = 0
    while True:
        player_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ")
        player_choice = player_choice.lower()
        if player_choice == 'quit':
            print("Thanks for playing!")
            break
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        if result == "win":
            print("You win!")
            wins += 1
        elif result == "lose":
            print("You lose!")
            losses += 1
        else:
            print("It's a tie!")
            ties += 1

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

    print(f"Final score: {wins} Wins, {losses} Losses, {ties} Ties")

if __name__ == "__main__":
    play_game()
