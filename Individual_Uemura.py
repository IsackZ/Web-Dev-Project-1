#Uemura Project
p1Name = input("What is your name (player 1)")
p2Name = input("What is your name (player 2)")
p1 = input("1 (Rock), 2 (Paper), or 3 (Scissors)")
p2 = input("1 (Rock), 2 (Paper), or 3 (Scissors)")
"""p1Wins = 0
p2Wins = 0"""

def gameWinP1():
    print(p1Name + " WINS")
def gameWinP2():
    print(p2Name + " WINS")
def gameDraw():
    print("YOU BOTH LOSE")
def playgame():
    #game draw
    if p1 == p2:
        gameDraw()
    #P2 Win conditions
    elif int(p1) == 1 and int(p2) == 2:
        gameWinP2()
        """global p2Wins
        p2Wins +=1"""
    elif int(p1) == 2 and int(p2) == 3:
        gameWinP2()
        """global p2Wins
        p2Wins +=1"""
    elif int(p1)==3 and int(p2)==1:
        gameWinP2()
        """global p2Wins
        p2Wins +=1"""
    #P1 Win conditions
    elif int(p1)==1 and int(p2)==3:
        gameWinP1()
        """global p1Wins
        p1Wins +=1"""
    elif int(p1)==2 and int(p2)==1:
        gameWinP1()
        """global p1Wins
        p1Wins +=1"""
    elif int(p1) == 3 and int(p2) == 2:
        gameWinP1()
        """global p1Wins
        p1Wins +=1"""
    else:
        print("error")
    
playgame()
"""def playagain():
    PA = input("Play Again?")
    if PA == "y":
        playgame()
    else:
        scores=input("Thanks for playing, print scores?")
        if scores == "y":
            print(p1Wins)
            print(p2Wins)
        else:
            print(ok)
playagain()"""
