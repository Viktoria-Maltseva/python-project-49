from random import randint
import math


def ask():
    return 'Answer "yes" if given number is prime. Otherwiseanswer "no".'


def question():
    return randint(0, 100)


def get_answer(question):
    right_answer = ''
    for i in range(2, int(math.sqrt(question)) + 1, 1):
        if question % i == 0:
            right_answer = 'no'
            break
    if right_answer == '':
        right_answer = 'yes'
    return right_answer


def count_answers(question, answer):
    count = 0
    question = get_answer(question)
    if question == answer:
        count = 1
    else:
        count = 5
    return count
