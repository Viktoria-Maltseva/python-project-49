from random import randint
import math


def ask_question():
    return 'Answer "yes" if given number is prime. Otherwiseanswer "no".'


def generate_task():
    return randint(0, 100)


def get_right_answer(task):
    right_answer = ''
    for i in range(2, int(math.sqrt(task)) + 1, 1):
        if task % i == 0:
            right_answer = 'no'
            break
    if right_answer == '':
        right_answer = 'yes'
    return right_answer


def count_answers(task, answer):
    count = 0
    right_answer = get_right_answer(task)
    if right_answer == answer:
        count = 1
    else:
        count = 5
    return count
