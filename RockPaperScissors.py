import random

while True:
    user_action = input("Enter a Choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You Win!")
        else:
            print("Paper covers rock! You Lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You Lose.")
        else:
            print("Paper covers rock! You Win!")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You Win!")
        else:
            print("Rock smashes scissors! You Lose.")

    play_again = input("Play Again? (y/n): ")
    if play_again.lower() != "y":
        break
