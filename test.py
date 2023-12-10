import random

def func(winDifference, lastChoice, lastRoundWL):
    # winDifference from -4 to 4
    # lastChoice from 1 to 3, 1 means paper, 2 means scissors, 3 means stone
    # lasrRound WL from 0 to 2, 0 means draw, 1 means win, 2 means loss
    return random.randint(1, 3)


def test_func():
    # Test with winDifference = -4, lastChoice = 1, lastRoundWL = 0
    result = func(-4, 1, 0)
    assert result in [1, 2, 3], "Test 1 failed"

    # Test with winDifference = 0, lastChoice = 2, lastRoundWL = 1
    result = func(0, 2, 1)
    assert result in [1, 2, 3], "Test 2 failed"

    # Test with winDifference = 4, lastChoice = 3, lastRoundWL = 2
    result = func(4, 3, 2)
    assert result in [1, 2, 3], "Test 3 failed"

    # Test with winDifference = 2, lastChoice = 1, lastRoundWL = 0
    result = func(2, 1, 0)
    assert result in [1, 2, 3], "Test 4 failed"

    # Test with winDifference = -3, lastChoice = 2, lastRoundWL = 1
    result = func(-3, 2, 1)
    assert result in [1, 2, 3], "Test 5 failed"

    print("All tests passed")

test_func()