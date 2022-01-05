from random import randint

player_options = ["Snape", "Nagini", "Neville"]

computer = player_options[randint(0,2)]

player = False

while player == False:
    player = input("Make your choice! Snape, Nagini or Neville? ")
    if player == computer:
        print("Computer chose", computer, "- It's a tie!")
    elif player == "Snape":
        if computer == "Nagini":
            print("Computer chose", computer, "- You lose!", computer, "eats", player)
        else:
            print("Computer chose", computer, "- You win!", player, "gives detention to", computer)
    elif player == "Nagini":
        if computer == "Neville":
            print("Computer chose", computer, "- You lose!", computer, "beheads", player)
        else:
            print("Computer chose", computer, "- You win!", player, "eats", computer)
    elif player == "Neville":
        if computer == "Snape":
            print("Computer chose", computer, "- You lose!", computer, "gives detention to", player)
        else:
            print("Computer chose", computer, "- You win!", player, "beheads", computer)
    else:
        print("That's not a valid play. Check your spelling!")

    player = False
    computer = player_options[randint(0,2)]
