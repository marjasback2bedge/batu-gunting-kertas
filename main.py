import random
from enum import Enum
import time

def func(winDifference, lastChoice, lastRoundWL):
    # winDifference from -4 to 4
    # lastChoice from 1 to 3, means whats the last choice from opponent, 1 means paper, 2 means scissors, 3 means stone
    # lasrRound WL from 0 to 2, 0 means draw, 1 means win, 2 means loss
    return random.randint(1, 3)

class Choice(Enum):
    PAPER = 1
    SCISSORS = 2
    STONE = 3

def main():
    player1_wins = 0
    player2_wins = 0
    tmpPlayer1_choice = 0
    tmpPlayer2_choice = 0
    winState1 = 0
    winState2 = 0
    while player1_wins < 5 and player2_wins < 5:
        input("Press any buttom to continue")
        player1_choice = func(player2_wins - player1_wins, tmpPlayer2_choice, winState1)
        player2_choice = func(player1_wins - player2_wins, tmpPlayer1_choice, winState2)
        tmpPlayer1_choice = player1_choice
        tmpPlayer2_choice = player2_choice
        print(f"Group1: {Choice(player1_choice).name}")
        time.sleep(2)
        print(f"Group2: {Choice(player2_choice).name}")
        time.sleep(2)
        winState1 = 0 
        winState2 = 0
        if player1_choice == player2_choice:
            print("Draw!")
        elif (player1_choice == 1 and player2_choice == 3) or (player1_choice == 2 and player2_choice == 1) or (player1_choice == 3 and player2_choice == 2):
            player1_wins += 1
            winState1 = 1
            winState2 = 2
            print("Group1 wins!")
        else:
            player2_wins += 1
            winState2 = 1
            winState1 = 2
            print("Group2 wins!")
        time.sleep(2)
        print(f"\nGroup1 won {player1_wins}, and Group2 won {player2_wins}\n")

    if player1_wins == 5:
        print("Group1 won the game!")
    else:
        print("Group2 won the game!")

main()  

