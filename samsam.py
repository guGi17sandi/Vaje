import random

options = ("Rock", "Paper", "Scissors")
player = None
computer = random.choice(options)
running = True
while running:

    while player not in options:
        player = input("Enter Rock, Paper or Scissors: ")
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Its a tie")
    elif player == "Rock" and computer == "Scissors":
        print("You win")
    elif player == "Paper" and computer == "Rock":
        print("You win")
    elif player == "Scissors" and computer == "Paper":
        print("You win")
    else:
        print("You lose")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

    print("Thanks for playing")