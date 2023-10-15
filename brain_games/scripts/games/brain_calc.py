from random import randint


def ask():
    return 'What is the result of the expression?'


def question():
    action = "*+-"[randint(0, 2)]
    number_1 = randint(0, 100)
    number_2 = randint(0, 100)
    s = f"{number_1} {action} {number_2}"
    return s


def get_answer(question):
    if question[3] != " ":
        action = question[3]
        number_1 = int(question[0:2])
        number_2 = int(question[5:])
    else:
        action = question[2]
        number_1 = int(question[0])
        number_2 = int(question[4:])

    match action:
        case "*":
            return number_1 * number_2
        case "+":
            return number_1 + number_2
        case "-":
            return number_1 - number_2
        case _:
            pass


def count_answers(expression, answer):
    count = 0
    right_answer = get_answer(expression)
    if right_answer == int(answer):
        count = 1
    else:
        count = 5
    return count
