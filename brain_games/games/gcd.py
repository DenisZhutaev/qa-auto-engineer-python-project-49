import math
import random

WELCOME_MESSAGE = "Welcome to the Brain Games!"
INSTRUCTION = "Find the greatest common divisor of given numbers."


def generate_question():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    question = f"{a} {b}"
    answer = str(math.gcd(a, b))
    return question, answer


def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer
