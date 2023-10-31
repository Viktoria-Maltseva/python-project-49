import prompt


def run(game_name):
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!", end='')
    print(game_name.ask_question())
    for correct_answers in range(3):
        task = game_name.generate_task()
        print(f"Question: {task}")
        answer = prompt.string("Your answer: ")
        correct_answer = game_name.is_correct(task, answer)
        if not correct_answer:
            print(f"'{answer}' is wrong answer ;(. "
                  + f"Correct answer was '{game_name.get_right_answer(task)}'")
            return print(f"Let's try again, {name}!")
        print("Correct!")
    return print(f"Congratulations, {name}!")
