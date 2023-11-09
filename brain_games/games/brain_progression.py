from random import randint


def import_functions():
    return ask_question, generate_task, get_right_answer, is_correct


def ask_question():
    return "What number is missing in the progression?"


def generate_task():
    step = randint(-10, 11)
    length = randint(5, 11)
    numbers = [randint(0, 100)]
    numbers.extend((numbers[i - 1] + step) for i in range(1, length, 1))
    index = randint(0, length - 1)
    numbers[index] = '..'
    string = ' '.join(str(num) for num in numbers)
    return string


def get_right_answer(task):
    numbers = task.split(' ', -1)
    right_answer = 0
    index = numbers.index('..')
    step = 0
    if index < (len(numbers) - 1) / 2:
        step = int(numbers[index + 2]) - int(numbers[index + 1])
        right_answer = int(numbers[index + 1]) - step
    else:
        step = int(numbers[index - 1]) - int(numbers[index - 2])
        right_answer = int(numbers[index - 1]) + step
    return right_answer


def is_correct(task, answer):
    try:
        if get_right_answer(task) == int(answer):
            return True
    except ValueError:
        pass
    return False
