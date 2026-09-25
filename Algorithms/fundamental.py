def exchange_values(a, b):
    return b,a

def count_numbers(n):
    count = 0

    for i in range(1, n + 1):
        count += 1

    return count

def summation(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

def fibonacci_sequence(n):
    sequence = []
    a = 0
    b = 1

    for i in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence


def reverse_number(n):
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10

    return reverse


def character_to_number(character):
    if character >= '0' and character <= '9':
        return ord(character) - ord('0')
    else:
        return None
