from random import randint
import math


def ask():
    return 'Find the greatest common divisor of given numbers.'


def question():
    number_1 = randint(0, 100)
    number_2 = randint(0, 100)
    s = f"{number_1} {number_2}"
    return s


def get_answer(question):
    number_1 = 0
    number_2 = 0
    index = 0
    for sym in question:
        if sym == ' ':
            break
        index += 1
    number_1 = int(question[: index])
    number_2 = int(question[index + 1:])
    return math.gcd(number_1, number_2)


def count_answers(expression, answer):
    count = 0
    expression = get_answer(expression)
    if expression == int(answer):
        count += 1
    else:
        count += 5
    return count
