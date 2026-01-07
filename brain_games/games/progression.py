import random

WELCOME_MESSAGE = "Welcome to the Brain Games!"
INSTRUCTION = "What number is missing in the progression?"


def generate_question():
    length = random.randint(5, 10)
    start = random.randint(1, 50)
    step = random.randint(2, 10)

    hidden_position = random.randint(0, length - 1)
    hidden_value = start + hidden_position * step

    progression = []
    for i in range(length):
        value = start + i * step
        if i == hidden_position:
            progression.append("..")
        else:
            progression.append(str(value))

    question = " ".join(progression)
    return question, str(hidden_value)


def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer
