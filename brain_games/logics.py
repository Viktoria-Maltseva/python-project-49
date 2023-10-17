from brain_games.scripts.brain_games import main
import brain_games.scripts.games.brain_even
import brain_games.scripts.games.brain_calc
import brain_games.scripts.games.brain_gcd
import brain_games.scripts.games.brain_progression
import brain_games.scripts.games.brain_prime


def run(game_name):
    module = __import__(f'brain_games.scripts.games.{game_name}',
                        fromlist=[game_name])
    name = main()
    print(module.ask())
    correct_answers = 0
    while (correct_answers < 3):
        question = module.question()
        print(f"Question: {question}")
        print("Your answer: ", end='')
        answer = input()
        correct_answers += module.count_answers(question, answer)
        if correct_answers < 5:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. " +
                  f"Correct answer was '{module.get_answer(question)}'")
            print(f"Let's try again, {name}!")

    if (correct_answers == 3):
        print(f"Congratulation, {name}!")
