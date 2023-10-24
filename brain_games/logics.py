from brain_games.scripts.brain_games import main


def run(game_name):
    module = __import__(f'brain_games.scripts.games.{game_name}',
                        fromlist=[game_name])
    name = main()
    print(module.ask_question())
    correct_answers = 0
    while (correct_answers < 3):
        task = module.generate_task()
        print(f"Question: {task}")
        print("Your answer: ", end='')
        answer = input()
        correct_answers += module.count_answers(task, answer)
        if correct_answers < 5:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  + f"Correct answer was '{module.get_right_answer(task)}'")
            print(f"Let's try again, {name}!")

    if (correct_answers == 3):
        print(f"Congratulations, {name}!")
