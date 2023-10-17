#!/usr/bin/env python3
from random import randint
from brain_games.scripts.brain_games import main, name
import math


def main():
    name = main()
    print("Find the greatest common divisor of given numbers.")
    correct_answers = 0
    while (correct_answers < 3):
        number_1 = randint(0, 100)
        number_2 = randint(0, 100)
        print(f"Question: {number_1} {number_2}")
        print("Your answer: ", end='')
        answer = input()
        try:
            answer = int(answer)
        except ValueError:
            print("The answer must be an integer number!")
            break
        if math.gcd(number_1, number_2) == int(answer):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. " +
                  f"Correct answer was '{math.gcd(number_1, number_2)}'")
            print(f"Let's try again, {name}!")
            correct_answers += 5
    if correct_answers == 3:
        print(f"Congratulation, {name}!")


if __name__ == "__main__":
    main()
