def decimal_to_base(number, base):
    if number == 0:
        return "0"

    digits = "0123456789ABCDEF"
    result = ""

    while number > 0:
        remainder = number % base
        result = digits[remainder] + result
        number //= base

    return result


def base_to_decimal(number, base):
    digits = "0123456789ABCDEF"
    number = number.upper()

    result = 0

    for digit in number:
        value = digits.index(digit)
        result = result * base + value

    return result


