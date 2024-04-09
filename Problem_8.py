while True:
    player1 = input("Player 1: Rock, Paper, or Scissors? ").lower()
    player2 = input("Player 2: Rock, Paper, or Scissors? ").lower()

    if player1 == player2:
        print("It's a tie!")
    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "scissors" and player2 == "paper") or \
         (player1 == "paper" and player2 == "rock"):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

    play_again = input("Do you want to play again? (yes/no) ").lower()
    if play_again == "no":
        print("Thanks for playing!")
        break
