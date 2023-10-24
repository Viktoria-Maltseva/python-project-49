from random import randint


def ask_question():
    return 'What is the result of the expression?'


def generate_task():
    action = "*+-"[randint(0, 2)]
    number_1 = randint(0, 100)
    number_2 = randint(0, 100)
    s = f"{number_1} {action} {number_2}"
    return s


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


def count_answers(task, answer):
    count = 0
    right_answer = get_right_answer(task)
    try:
        if right_answer == int(answer):
            count = 1
        else:
            count = 5
    except ValueError:
        count = 5
    return count
