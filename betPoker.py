#!/usr/bin/python3

import random

fullDeck = ["2C","3C","4C","5C","6C","7C","8C","9C","10C","AC","KC","JC","QC","2D","3D","4D","5D","6D","7D","8D","9D","10D","AD","KD","JD","QD","2H","3H","4H","5H","6H","7H","8H","9H","10H","AH","KH","JH","QH","2S","3S","4S","5S","6S","7S","8S","9S","10S","AS","KS","JS","QS"]

usercards=[]
dealtCards=[]
suitCount = 0
suit=["C","D","H","S"]
rank=["2","3","4","5","6","7","8","9","0","A","K","J","Q"]
rankScore={"2":1,"3":2,"4":3,"5":4,"6":5,"7":6,"8":7,"9":8,"0":9,"A":13,"K":12,"J":10,"Q":11}
handSuit=[]
handRank=[]
checkWin=[]


def dealhand():
    while len(usercards) < 5:
        deal = random.choice(fullDeck)
        usercards.append(deal)
        dealtCards.append(deal)
        fullDeck.remove(deal)


def display():
    print("----------Your hand:----------")
    print(usercards)
    print("- #1    #2    #3    #4    #5 -")
    #print("Money: $", playerMoney)
    
def discard():
    dcValues={"1":0,"2":1,"3":2,"4":3,"5":4}
    chooseDiscard=input("Use numbers to discard: ")
    if len(chooseDiscard) > 0:
        for num in chooseDiscard:
            usercards.pop(dcValues[num])
            newCard=random.choice(fullDeck)
            fullDeck.remove(newCard)
            dealtCards.append(newCard)
            usercards.insert(dcValues[num], newCard)
        

def sortHand():
    for x in usercards:
        card = x
        for y in card:
            if y in rank:
                handRank.append(y)
            if y in suit:
                handSuit.append(y)
    handRank.sort()

def scoreHand():
    counter=0
    counterTwo=0
    counterThree=0
    pairTest = " " 
    firstPair = []
    secondPair = []
    strtScore = []
    strtTest = 0
    flushTest = handSuit[0]
    for f in handSuit:
        if f == flushTest:
            counterThree+=1
    for r in handRank:
        if r == pairTest:
            counter += 1
            #firstPair will have 2 items if triple
            if counter > 1 and r not in firstPair:
                secondPair.append(r)
            else:
                firstPair.append(r)
        pairTest = r
        #print (pairTest)
    for n in handRank:
        strtScore.append(rankScore[n])
    strtScore.sort()
    strtTest = strtScore[0] - 1
    for s in strtScore:
        if s == strtTest + 1:
            counterTwo += 1
        strtTest = s
    #    print(rankScore[s])
    #   print(straightTest,"the test")
    scoreHand = ["Pair", "Two Pair","Three of a Kind!","Straight!","Flush!","Full House!!","Four of a kind!!","Straight Flush!!","Royal Flush!?!"]
    playerScore = " "
    if counterTwo == 5 and counterThree == 5:
        if strtScore[4] == 13:
            playerScore = scoreHand[8]
            checkWin.append(7)
        else:
            playerScore = scoreHand[7]
            checkWin.append(6)
    elif counter == 3 and len(secondPair) == 0:
        playerScore = scoreHand[6]
        checkWin.append(5)
    elif counter == 3 and len(secondPair) >= 1:
        playerScore = scoreHand[5]
        checkWin.append(5)
    elif counterThree == 5:
        playerScore = scoreHand[4]
        checkWin.append(4)
    elif counterTwo == 5:
        playerScore = scoreHand[3]
        checkWin.append(4)
    elif counter == 2 and len(firstPair) >= 2:
        playerScore = scoreHand[2]
        checkWin.append(3)
    elif counter == 2 and len(secondPair) == 1:
        playerScore = scoreHand[1]
        checkWin.append(2) 
    elif counter == 1:
        playerScore = scoreHand[0]
        checkWin.append(1)
        #checkWin.append(1)
        #playerMoney = playerMoney + (betValue * 2)
    else:
        playerScore = "...sorry, nothing."
    print("Your hand is a",playerScore)

def main():
    print("-------5 Card Draw Poker--------")
    print("Winnings: Pair X0.5 Two Pair X2")
    print("Three of a Kind X3 Flush/Straight X5")
    print("Four Kind/Full House X6 Straight Flush X10")
    print("Royal Flush X100")
    playGame = True
    playerMoney=100
    while playGame == True:
        #dealhand()
        #display()
        print("Your cash: $",playerMoney)
        playerBet=input("Place your bet: $")
        betCheck=int(playerBet)
        betValue=0
        while betCheck > playerMoney:
            betAgain=input("You don't have that much cash! Try again: $")
            betCheck=int(betAgain)
            betValue=betCheck
        else:
            betValue=betCheck
        playerMoney= playerMoney - betValue
        print("Bet: $",betValue,"Cash remaining: $",playerMoney)
        dealhand()
        display()
        discard()
        sortHand()
        scoreHand()
        winnings= 0
        for win in checkWin:
            if win == 1: #Pair
                winnings= betValue // 2 
                playerMoney = playerMoney + winnings
            elif win == 2: # 2 pair
                winnings= betValue * 2
                playerMoney = playerMoney + winnings
            elif win == 3: # three of a kind
                winnings= betValue * 3
                playerMoney = playerMoney + winnings
            elif win == 4: #flush straight
                winnings= betValue * 5
                playerMoney = playerMoney + winnings
            elif win == 5: #full house four
                winnings= betValue * 6
                playerMoney = playerMoney + winnings
            elif win == 6:#straight flush
                winnings= betValue * 10
                playerMoney = playerMoney + winnings
            elif win == 7:#royal flush
                winnings == betValue * 100
                playerMoney = playerMoney + winnings
            else:
                pass
        display()
        print("You won: $",winnings)
        print("$",playerMoney)
        usercards.clear()
        checkWin.clear()
        handSuit.clear()
        handRank.clear()
        fullDeck.extend(dealtCards)
        dealtCards.clear()
        if playerMoney <= 0:
            print("Out of cash! Game over")
            playGame == False
            break
        else:
            pass
        playAgain=input("Enter to deal again. q to quit: ")
        if playAgain == "q":
            playGame == False
            break
        else:
            continue

if __name__ == "__main__":
    main()


