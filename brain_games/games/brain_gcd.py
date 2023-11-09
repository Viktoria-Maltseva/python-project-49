from random import randint
import math


def import_functions():
    return ask_question, generate_task, get_right_answer, is_correct


def ask_question():
    return 'Find the greatest common divisor of given numbers.'


def generate_task():
    return f"{randint(0, 100)} {randint(0, 100)}"


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


def is_correct(task, answer):
    try:
        if get_right_answer(task) == int(answer):
            return True
    except ValueError:
        pass
    return False
