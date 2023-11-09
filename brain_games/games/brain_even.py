from random import randint
import sys


def import_functions():
    return ask_question, generate_task, get_right_answer, is_correct


def ask_question():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_task():
    return randint(-sys.maxsize - 1, sys.maxsize)


def get_right_answer(task):
    return task % 2 and 'no' or 'yes'


def is_correct(number, answer):
    if get_right_answer(number) == answer:
        return True
    else:
        return False
