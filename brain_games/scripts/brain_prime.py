#!/usr/bin/env python3
from random import randint
import math
import brain_games.scripts.brain_games


def prime(number):
    right_answer = ''
    for i in range(2, int(math.sqrt(number)) + 1, 1):
        if number % i == 0:
            right_answer = 'no'
            break
    if right_answer == '':
        right_answer = 'yes'
    return right_answer


def main():
    name = brain_games.scripts.brain_games.main()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count_answers = 0
    while count_answers < 3:
        number = randint(0, 100)
        print(f"Question: {number}")
        print("Your answer: ", end='')
        answer = input()
        right_answer = prime(number)
        if answer == right_answer:
            count_answers += 1
            print("Correct!")
        else:
            count_answers += 5
            print(f"'{answer}' is wrong answer ;(. "
                  + f"Correct answer was '{right_answer}'!")
            print(f"Let's try again, {name}!")
            break
    if count_answers == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
