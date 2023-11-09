from random import randint
import math


def import_functions():
    return ask_question, generate_task, get_right_answer, is_correct


def ask_question():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_task():
    return randint(2, 100)


def get_right_answer(task):
    right_answer = ''
    for i in range(2, int(math.sqrt(task)) + 1, 1):
        if task % i == 0:
            right_answer = 'no'
            break
    if right_answer == '':
        right_answer = 'yes'
    return right_answer


def is_correct(task, answer):
    if get_right_answer(task) == answer:
        return True
    else:
        return False
