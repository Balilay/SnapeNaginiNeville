import random

def play():
    user = input("Play your move: Snape, Neville, or Nagini? \n")
    computer = random.choice(['Snape', 'Neville', 'Nagini'])

    if user == computer:
        return 'It\'s a tie'
      
      
    # "Neville" > "Nagini", "Nagini" > "Snape", "Snape" > "Neville"
    if is_win(user, computer):
        return 'You won!'
    
def is_win(user, computer):
    # return true if player wins
    # '"Neville" > "Nagini", "Nagini" > "Snape", "Snape" > "Neville"
    if (player == 'Neville' and opponent == 'Nagini') or (player == 'Nagini' and opponent == 'Snape') \
        or (player == 'Snape' and opponent == 'Neville'):
        return True
    
    else:
    return 'You lost!'

print(play())
