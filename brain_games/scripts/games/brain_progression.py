from random import randint


def ask():
    return "What number is missing in the progression?"


def question():
    step = randint(-10, 11)
    length = randint(5, 11)
    numbers = [randint(0, 100)]
    numbers.extend((numbers[i - 1] + step) for i in range(1, length, 1))
    index = randint(0, length - 1)
    numbers[index] = '..'
    string = ' '.join(str(num) for num in numbers)
    return string


def get_answer(question):
    numbers = question.split(' ', -1)
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


def count_answers(number, answer):
    number = get_answer(number)
    count = 0
    if number == int(answer):
        count = 1
    else:
        count = 5
    return count
