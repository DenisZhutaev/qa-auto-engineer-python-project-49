import random

WELCOME_MESSAGE = "Welcome to the Brain Games!"
INSTRUCTION = "What is the result of the expression?"


def generate_question():
    operations = ["+", "-", "*"]
    operation = random.choice(operations)

    match operation:
        case "+":
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            question = f"{a} + {b}"
            answer = a + b
        case "-":
            a = random.randint(1, 100)
            b = random.randint(1, a)  # Ensure non-negative result
            question = f"{a} - {b}"
            answer = a - b
        case "*":
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            question = f"{a} * {b}"
            answer = a * b

    return question, str(answer)


def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer
