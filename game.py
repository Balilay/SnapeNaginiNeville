import random

def play():
    user = input("Play your move: Snape, Neville, or Nagini? \n")
    computer = random.choice(['Snape', 'Neville', 'Nagini'])
    
def is_win(user, computer):
    # return true if player wins
    # '"Neville" > "Nagini", "Nagini" > "Snape", "Snape" > "Neville"
    if (user == 'Neville' and computer == 'Nagini') or (user == 'Nagini' and computer == 'Snape') \
        or (user == 'Snape' and computer == 'Neville'):
        return True

    if user == computer:
        return "It's a tie"
      
    elif is_win(user, computer):
        return "You won!"
    
    else:
    return 'You lost!'

print(play())
