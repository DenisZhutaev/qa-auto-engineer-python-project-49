import random

WELCOME_MESSAGE = "Welcome to the Brain Games!"
INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2

    return True


def generate_question():
    number = random.randint(1, 100)
    question = str(number)
    answer = "yes" if is_prime(number) else "no"
    return question, answer


def check_answer(user_answer, correct_answer):
    return user_answer.lower() == correct_answer.lower()
