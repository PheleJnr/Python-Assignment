player_one = input("Enter (rock, paper, or scissor): ")

player_two = input("Enter (rock, paper, or scissor): ")

if player_one == "rock" and player_two == "paper":
		print("Player Two wins")

elif player_one == "paper" and player_two == "rock":
		print("Player One wins")

elif player_one == "paper" and player_two == "scissor":
		print("Player Two wins")

elif player_one == "scissor" and player_two == "paper":
		print("Player One wins")

elif player_one == "scissor" and player_two == "rock":
		print("Player Two wins")

elif player_one == "rock" and player_two == "scissor":
		print("Player One wins")

elif player_two == "rock" and player_one == "paper":
		print("Player One wins")

elif player_two == "paper" and player_one == "rock":
		print("Player Two wins")

elif player_two == "paper" and player_one == "scissor":
		print("Player One wins")

elif player_two == "scissor" and player_one == "paper":
		print("Player Two wins")

elif player_two == "scissor" and player_one == "rock":
		print("Player One wins")

elif player_two == "rock" and player_one == "scissor":
		print("Player Two wins")

elif player_one == player_two:
		print ("Tie")

elif player_two == player_one:
		print ("Tie")

else:
		print("invalid input")

