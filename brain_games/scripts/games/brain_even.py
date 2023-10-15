from random import randint
import sys


def ask():
    return 'Answer "yes" if the number is even, otherwise answer "no"'


def question():
    number = randint(-sys.maxsize - 1, sys.maxsize)
    return number


def get_answer(question):
    return question % 2 and 'no' or 'yes'


def count_answers(number, answer):
    count = 0
    if ((number % 2 == 0 and answer == 'yes') or
            (number % 2 == 1 and answer == 'no')):
        count = 1
    else:
        count = 5
    return count
