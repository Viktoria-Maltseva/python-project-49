from random import randint


def import_functions():
    return ask_question, generate_task, get_right_answer, is_correct


def ask_question():
    return 'What is the result of the expression?'


def generate_task():
    return f"{randint(0, 100)} {'*+-'[randint(0, 2)]} {randint(0, 100)}"


def get_right_answer(task):
    if task[3] != " ":
        action = task[3]
        number_1 = int(task[0:2])
        number_2 = int(task[5:])
    else:
        action = task[2]
        number_1 = int(task[0])
        number_2 = int(task[4:])

    match action:
        case "*":
            return number_1 * number_2
        case "+":
            return number_1 + number_2
        case "-":
            return number_1 - number_2
        case _:
            pass


def is_correct(task, answer):
    try:
        if get_right_answer(task) == int(answer):
            return True
    except ValueError:
        pass
    return False
