# SPRAWDŹ TO!!!!

# Checks if player inputs correct value: rock, scissors or paper. Returns true if so otherwise returns false
def checkInput(s):
    b = False
    if s:
        if s == "rock" or s=="scissors" or s== "paper":
            b = True
    return b

#assigns correct choice to the player
def setPlayerChoice (player, s):
    if checkInput(s):
        player = s
    else: print("You've entered wrong value")
    return player

#checks who is the winner
def whoWins (p1,p2):
    wins = ""
    if p1 == p2:
        print("It's tie. You've chosen same thing")
    elif p1 == "rock":
        if p2 == "scissors": wins = "Player 1"
        elif p2 == "paper": wins = "Player 2"
    elif p1 == "scissors":
        if p2 == "rock": wins = "Player 2"
        elif p2 == "paper": wins = "Player 1"
    elif p1 == "paper":
        if p2 == "scissors":wins = "Player 2"
        elif p2 =="rock": wins = "Player 1"
    return wins

print("Welcome to the ROCK PAPER SCISSORS GAME!!\n You must choose one of the following:\n...rock...\n...paper...\n...scissors...")
player1, player2 = None, None
while not player1:
    s = input("Player's 1 choice: ")
    player1 = setPlayerChoice(player1, s)
print("********************\n*********************\n!!!!!Don't look at player 1 choice!!!!!\n********************\n********************\n"*6)
while not player2:
    s = input("Player's 2 choice: ")
    player2 = setPlayerChoice(player2, s)
print("SHOOT")
print("Player 1 choice: "+player1+" Player 2 choice: "+player2)
if whoWins(player1,player2):
    print("AND THE WINNER IS .... \n"+ whoWins(player1, player2))
#options = ["rock","scissors","paper"]
#for o in options:
#    for k in options:
#        print("player 1: "+o+" player 2: "+k)
#        print(whoWins(o,k))
#        
#    
          

