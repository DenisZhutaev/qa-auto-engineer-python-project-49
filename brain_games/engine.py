import prompt


def run_game(game_module, rounds=3):
    
    print(game_module.WELCOME_MESSAGE)
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game_module.INSTRUCTION)

    for _ in range(rounds):
        question, correct_answer = game_module.generate_question()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if not game_module.check_answer(user_answer, correct_answer):
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'. "
                f"Let's try again, {name}!"
            )
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
