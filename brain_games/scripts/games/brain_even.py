from random import randint
import sys


def ask_question():
    return 'Answer "yes" if the number is even, otherwise answer "no"'


def generate_task():
    number = randint(-sys.maxsize - 1, sys.maxsize)
    return number


def get_right_answer(task):
    return task % 2 and 'no' or 'yes'


def count_answers(number, answer):
    count = 0
    if ((number % 2 == 0 and answer == 'yes')
            or (number % 2 == 1 and answer == 'no')):
        count = 1
    else:
        count = 5
    return count
