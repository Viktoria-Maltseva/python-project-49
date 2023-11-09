import prompt


def run_game(ask_question, generate_task, get_right_answer, is_correct):
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!", end='\n')
    print(ask_question())
    number_rounds = 3
    for correct_answers in range(number_rounds):
        task = generate_task()
        print(f"Question: {task}")
        answer = prompt.string("Your answer: ")
        correct_answer = is_correct(task, answer)
        if correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{get_right_answer(task)}'")
            return print(f"Let's try again, {name}!")
    return print(f"Congratulations, {name}!")
