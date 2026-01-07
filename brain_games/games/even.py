import random

WELCOME_MESSAGE = "Welcome to the Brain Games!"
INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question():
    number = random.randint(1, 100)
    question = str(number)
    answer = "yes" if is_even(number) else "no"
    return question, answer


def is_even(number):
    return number % 2 == 0


def check_answer(user_answer, correct_answer):
    return user_answer.lower() == correct_answer.lower()
