from random import randint
import math


def ask_question():
    return 'Find the greatest common divisor of given numbers.'


def generate_task():
    number_1 = randint(0, 100)
    number_2 = randint(0, 100)
    s = f"{number_1} {number_2}"
    return s


def get_right_answer(task):
    number_1 = 0
    number_2 = 0
    index = 0
    for sym in task:
        if sym == ' ':
            break
        index += 1
    number_1 = int(task[: index])
    number_2 = int(task[index + 1:])
    return math.gcd(number_1, number_2)


def count_answers(task, answer):
    count = 0
    right_answer = get_right_answer(task)
    try:
        if right_answer == int(answer):
            count += 1
        else:
            count += 5
    except ValueError:
        count += 5
    return count
