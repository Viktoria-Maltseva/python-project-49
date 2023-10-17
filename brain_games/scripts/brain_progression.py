#!/usr/bin/env python3
from random import randint
import brain_games.scripts.brain_games


def main():
    name = brain_games.scripts.brain_games.main()
    print("What number is missing in the progression?")
    correct_answers = 0
    while correct_answers < 3:
        step = randint(-10, 11)
        length = randint(5, 11)
        numbers = [randint(0, 100)]
        numbers.extend((numbers[i - 1] + step) for i in range(1, length, 1))
        index = randint(0, length - 1)
        closed_number = numbers[index]
        numbers[index] = '..'
        string = ' '.join(str(num) for num in numbers)
        print(f"Question: {string}")
        print("Your answer: ", end='')
        answer = input()
        try:
            answer = int(answer)
        except ValueError:
            print("The answer must be an integer number!")
            break
        if closed_number == answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer;(. " +
                  f"Correct answer was '{closed_number}'")
            print(f"Let's try again, {name}!")
            correct_answers += 5

    if correct_answers == 3:
        print(f"Congratulation, {name}!")


if __name__ == "__main__":
    main()
