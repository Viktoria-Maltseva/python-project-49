from random import randint
import math
from brain_games.engine import run_game


def start_the_game():
    run_game(ask_question, generate_task, get_right_answer)


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
    return str(math.gcd(number_1, number_2))
