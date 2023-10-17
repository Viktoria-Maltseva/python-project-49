#!/usr/bin/env python3
from random import randint
import sys
from brain_games.scripts.brain_games import main, name


def main():
    name = brain_games.scripts.brain_games.main()
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    correct_answers = 0
    while (correct_answers < 3):
        number = randint(-sys.maxsize - 1, sys.maxsize)
        print(f"Question: {number}")
        print("Your answer: ", end='')
        answer = input()
        if ((number % 2 == 0 and answer == 'yes') or
                (number % 2 == 1 and answer == 'no')):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. " +
                  f"Correct answer was '{number % 2 and 'no' or 'yes'}'")
            print(f"Let's try again, {name}!")
            correct_answers = 5
    if (correct_answers == 3):
        print(f"Congratulations, {name}")


if __name__ == "__main__":
    main()
