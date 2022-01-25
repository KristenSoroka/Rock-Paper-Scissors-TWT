#best practice to import items at the beginning
import random

# starting the game with no wins
user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']  #list

# allow the user to input rock, paper, scissors, or 'q' to quit the game
while True:
  user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
  if user_input == 'q':
    #quit()  #the whole program will quit.
    break #break out of the while loop w/o quitting whole program
  if user_input not in options: 
    continue 
    #a keyword that will allow start will start the loop over
  random_number =random.randint(0, 2)  
  #randint both stop and start values included 
  # rock: 0, paper: 1, scissors: 2 
  computer_pick = options[random_number]
  print(f"Computer picked {computer_pick}.")

  if user_input == "rock" and computer_pick == "scissors":
    print("You won!")
    user_wins += 1
  elif user_input == "paper" and computer_pick == "rock":
    print("You won!")
    user_wins += 1
  elif user_input == "scissors" and computer_pick == "paper":
    print("You win!")
    user_wins += 1
  elif user_input == computer_pick:
    print("Draw!")
  else:
    print("You lost!")
    computer_wins += 1
    

print(f"You won {user_wins} times.")
print(f"The computer won {computer_wins} times.")
print("goodbye") #will print if you quit the game
