#!/usr/bin/env python3
from random import randint
import brain_games.scripts.brain_games


def main():
    name = brain_games.scripts.brain_games.main()
    print("What is the result of the expression?.")
    correct_answers = 0
    while (correct_answers < 3):
        action = "*+-"[randint(0, 2)]
        number_1 = randint(0, 100)
        number_2 = randint(0, 100)
        print(f"Question: {number_1} {action} {number_2}")
        print("Your answer: ", end='')
        answer = input()
        try:
            answer = int(answer)
        except ValueError:
            print("The answer must be an integer number!")
            break
        match action:
            case "*":
                if ((number_1 * number_2) == int(answer)):
                    print("Correct!")
                    correct_answers += 1
                else:
                    print(f"'{answer}' is wrong answer ;(. "
                          + f"Correct answer was '{number_1 * number_2}'")
                    print(f"Let's try again, {name}!")
                    correct_answers = 5
            case "+":
                if ((number_1 + number_2) == int(answer)):
                    print("Correct!")
                    correct_answers += 1
                else:
                    print(f"'{answer}' is wrong answer ;(. "
                          + f"Correct answer was '{number_1 + number_2}'")
                    print(f"Let's try again, {name}!")
                    correct_answers = 5
            case "-":
                if ((number_1 - number_2) == int(answer)):
                    print("Correct!")
                    correct_answers += 1
                else:
                    print(f"'{answer}' is wrong answer ;(. "
                          + f"Correct answer was '{number_1 - number_2}'")
                    print(f"Let's try again, {name}!")
                    correct_answers = 5
            case _:
                break
    if (correct_answers == 3):
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
