import random


def square_root(n):
    if n < 0:
        return None

    guess = n

    if n == 0:
        return 0

    for _ in range(20):
        guess = (guess + n / guess) / 2

    return guess


def smallest_divisor(n):
    if n < 2:
        return None

    divisor = 2

    while divisor * divisor <= n:
        if n % divisor == 0:
            return divisor
        divisor += 1

    return n


def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return abs(a)


def generate_primes(n):
    primes = []

    for number in range(2, n + 1):
        is_prime = True

        divisor = 2

        while divisor * divisor <= number:
            if number % divisor == 0:
                is_prime = False
                break
            divisor += 1

        if is_prime:
            primes.append(number)

    return primes


def prime_factors(n):
    factors = []
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1

    return factors


def pseudo_random_number(start, end):
    return random.randint(start, end)


def large_power(base, exponent):
    result = 1

    while exponent > 0:
        if exponent % 2 == 1:
            result *= base

        base *= base
        exponent //= 2

    return result


def nth_fibonacci(n):
    if n < 0:
        return None

    a = 0
    b = 1

    for _ in range(n):
        a, b = b, a + b

    return a

