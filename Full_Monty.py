"""Monty Hall Problem"""

import random


def monty(guess, change=True):
    # Takes a guess (int between 1 and 3) and a change value (boolian true/false).
    # A correct answer is chosen at random (also an int between 1 and 3).
    # One int between 1 and 3 which does not match either the guess or correct answer will be eliminated.
    # If change is true the guess will change to the only remaining int after one incorrect value is eliminated.
    rightdoor = random.randint(1, 3)
    remdoor = random.randint(1, 3)
    # if the guess is right the first time, eliminate a door at random from the remaining two.
    if rightdoor == guess:
        if remdoor == guess:
            while remdoor == guess:
                remdoor = random.randint(1, 3)
    # if the guess is wrong the first time, eliminate the only remaining wrong door.
    elif rightdoor != guess:
        for i in [1, 2, 3]:
            if i != rightdoor and i != guess:
                remdoor = i
    # list the two remaining doors after the elimination of one wrong door
    doorsremaining = []
    for i in range(1, 4):
        if i != remdoor:
            doorsremaining.append(i)
    # if we decide to change doors after one is eliminated.
    if change:
        doorsremaining.remove(guess)
        guess = doorsremaining[0]
    # find out if the guess is the correct answer.
    if guess == rightdoor:
        success = True
    else:
        success = False
    return success


def run_doortest(iterations, change=True):
    # Takes a desired number of iterations to run and a change value (as above).
    # Runs the Monty Hall Problem three times for each iteration (once with each possible guess; 1, 2 or 3).
    # Returns the percentage of times the answer was correct.
    wincount = 0
    for door in range(1, 4):
        for it in range(iterations):
            if monty(door, change):
                wincount += 1
    wincount = wincount / 3
    percent = 100 / iterations
    wincount = wincount * percent
    return wincount


# Run 10,000 iterations of the Monty Hall Problem, with each possible guess, changing door when one is eliminated.
print(run_doortest(10000, True))
# Run 10,000 iterations of the Monty Hall Problem, with each possible guess, not changing door when one is eliminated.
print(run_doortest(10000, False))
