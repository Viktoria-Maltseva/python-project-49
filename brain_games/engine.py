import prompt


NUMBER_ROUNDS = 3


def run_game(ask_question, generate_task, get_right_answer):
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!\n{ask_question()}", end='\n')
    for _ in range(NUMBER_ROUNDS):
        task = generate_task()
        print(f"Question: {task}")
        answer = prompt.string("Your answer: ")
        correct_answer = get_right_answer(task)
        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{get_right_answer(task)}'\n"
                  f"Let's try again, {name}!")
            return
    return print(f"Congratulations, {name}!")
