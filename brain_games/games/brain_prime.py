from random import randint
import math
from brain_games.engine import run_game


def start_the_game():
        run_game(ask_question, generate_task, get_right_answer)


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
    return str(right_answer)
