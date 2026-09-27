import random


def generate_factorial_question():
    number = random.randint(3, 8)
    answer = 1

    for i in range(1, number + 1):
        answer *= i

    return f"What is the factorial of {number}?", answer


def generate_sum_question():
    number = random.randint(5, 20)
    answer = 0

    for i in range(1, number + 1):
        answer += i

    return f"What is the sum of numbers from 1 to {number}?", answer


def generate_gcd_question():
    a = random.randint(10, 50)
    b = random.randint(10, 50)

    x = a
    y = b

    while y != 0:
        x, y = y, x % y

    return f"What is the GCD of {a} and {b}?", x


def generate_question():
    question_type = random.randint(1, 3)

    if question_type == 1:
        return generate_factorial_question()

    elif question_type == 2:
        return generate_sum_question()

    else:
        return generate_gcd_question()