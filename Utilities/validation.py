def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_positive_integer(prompt):
    while True:
        try:
            number = int(input(prompt))

            if number > 0:
                return number

            print("Please enter a positive integer.")

        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_non_negative_integer(prompt):
    while True:
        try:
            number = int(input(prompt))

            if number >= 0:
                return number

            print("Please enter 0 or a positive integer.")

        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_integer_list(prompt):
    while True:
        try:
            numbers = list(map(int, input(prompt).split()))

            if numbers:
                return numbers

            print("Please enter at least one number.")

        except ValueError:
            print("Invalid input. Please enter integers separated by spaces.")