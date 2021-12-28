import random

user_action = input("Play your move! Snape, Nagini or Neville? ")

possible_actions = ["Snape", "Nagini", "Neville"]
computer_action = random.choice(possible_actions)
print("You chose " + str(user_action) + ", computer chose " + str(computer_action) + "\n") 

    if user_action == computer_action:
        print("Both players selected " + (user_move) + ". It's a tie!"
    elif user_action == "Snape":
          if computer_action == "Neville":
            print("Snape gives detention to Neville! You win!")
          else:
            print("Nagini eats Snape! You lose!")
    elif user_action == "Nagini":
          if computer_action == "Snape":
            print("Nagini eats Snape! You win!")
          else: 
            print("Neville beheads Nagini! You lose!")
    elif user_action == "Neville":
          if computer_action == "Snape":
            print("Snape gives detention to Neville! You lose!")
          else: 
            print("Neville beheads Nagini! You win!")
          
     

