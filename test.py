import random

def func(winDifference, lastChoice, lastRoundWL):
    # winDifference from -4 to 4
    # lastChoice from 1 to 3, 1 means paper, 2 means scissors, 3 means stone
    # lasrRound WL from 0 to 2, 0 means draw, 1 means win, 2 means loss



def test():
    for i in range(-4, 5):
        for j in range(1, 4):
            for k in range(0, 3):
                result = func(i, j, k)
                print(f"{i}, {j}, {k}")
                assert result in [1, 2, 3], f"Test {i}, {j}, {k} failed"
    print("All tests passed")    

test()
