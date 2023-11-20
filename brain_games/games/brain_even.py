from random import randint
import sys
from brain_games.engine import run_game


def start_the_game():
    run_game(ask_question, generate_task, get_right_answer)


def ask_question():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_task():
    return randint(-sys.maxsize - 1, sys.maxsize)


def get_right_answer(task):
    return str(task % 2 and 'no' or 'yes')
