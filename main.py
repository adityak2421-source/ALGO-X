from Algorithms import fundamental
from Algorithms import factoring
from Algorithms import arrays
from Algorithms import collections
from Algorithms import conversions
from Learning import explanations
from Practice import questions
from Utilities import validation
from Utilities import performance
from Utilities import history
from Utilities import file_manager


def show_menu():
    print("\n============================================")
    print("                    ALGO-X")
    print("        INTERACTIVE ALGORITHM TOOLKIT")
    print("============================================")
    print("1. Solve an Algorithm")
    print("2. Learn an Algorithm")
    print("3. Practice Mode")
    print("4. Performance Analysis")
    print("5. History")
    print("6. Help")
    print("7. Exit")
    print("============================================")


def save_operation(operation, details):
    history.add_history(operation, details)


def fundamental_menu():
    while True:
        print("\n========================================")
        print("       FUNDAMENTAL ALGORITHMS")
        print("========================================")
        print("1. Exchange Values")
        print("2. Counting")
        print("3. Summation")
        print("4. Factorial")
        print("5. Fibonacci Sequence")
        print("6. Reverse a Number")
        print("7. Character to Number")
        print("8. Back to Main Menu")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            a = validation.get_integer("Enter first value: ")
            b = validation.get_integer("Enter second value: ")

            result = fundamental.exchange_values(a, b)
            print("After exchange:", result)

            save_operation(
                "Exchange Values",
                f"a={a}, b={b}, result={result}"
            )

        elif choice == "2":
            n = validation.get_non_negative_integer("Enter a number: ")

            result = fundamental.count_numbers(n)
            print("Count:", result)

            save_operation(
                "Counting",
                f"n={n}, result={result}"
            )

        elif choice == "3":
            n = validation.get_non_negative_integer("Enter a number: ")

            result = fundamental.summation(n)
            print("Sum:", result)

            save_operation(
                "Summation",
                f"n={n}, result={result}"
            )

        elif choice == "4":
            n = validation.get_non_negative_integer("Enter a number: ")

            result = fundamental.factorial(n)
            print("Factorial:", result)

            save_operation(
                "Factorial",
                f"n={n}, result={result}"
            )

        elif choice == "5":
            n = validation.get_non_negative_integer(
                "How many Fibonacci numbers? "
            )

            result = fundamental.fibonacci_sequence(n)
            print("Fibonacci sequence:", result)

            save_operation(
                "Fibonacci Sequence",
                f"n={n}, result={result}"
            )

        elif choice == "6":
            n = validation.get_non_negative_integer("Enter a number: ")

            result = fundamental.reverse_number(n)
            print("Reversed number:", result)

            save_operation(
                "Reverse Number",
                f"n={n}, result={result}"
            )

        elif choice == "7":
            character = input("Enter a digit character: ")

            result = fundamental.character_to_number(character)
            print("Number:", result)

            save_operation(
                "Character to Number",
                f"character={character}, result={result}"
            )

        elif choice == "8":
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


def factoring_menu():
    while True:
        print("\n========================================")
        print("          FACTORING ALGORITHMS")
        print("========================================")
        print("1. Find Square Root")
        print("2. Find Smallest Divisor")
        print("3. Find GCD")
        print("4. Generate Prime Numbers")
        print("5. Find Prime Factors")
        print("6. Generate Pseudo-Random Number")
        print("7. Raise Number to Large Power")
        print("8. Find nth Fibonacci Number")
        print("9. Back to Algorithm Solver")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            n = validation.get_float("Enter a number: ")

            result = factoring.square_root(n)

            if result is None:
                print("Square root is not available for negative numbers.")
            else:
                print("Square root:", result)

                save_operation(
                    "Square Root",
                    f"n={n}, result={result}"
                )

        elif choice == "2":
            n = validation.get_integer("Enter an integer: ")

            result = factoring.smallest_divisor(n)

            if result is None:
                print("Please enter a number greater than 1.")
            else:
                print("Smallest divisor:", result)

                save_operation(
                    "Smallest Divisor",
                    f"n={n}, result={result}"
                )

        elif choice == "3":
            a = validation.get_integer("Enter first number: ")
            b = validation.get_integer("Enter second number: ")

            result = factoring.gcd(a, b)
            print("GCD:", result)

            save_operation(
                "GCD",
                f"a={a}, b={b}, result={result}"
            )

        elif choice == "4":
            n = validation.get_non_negative_integer(
                "Generate primes up to: "
            )

            result = factoring.generate_primes(n)
            print("Prime numbers:", result)

            save_operation(
                "Generate Primes",
                f"limit={n}, result={result}"
            )

        elif choice == "5":
            n = validation.get_positive_integer("Enter a number: ")

            result = factoring.prime_factors(n)

            if result:
                print("Prime factors:", result)

                save_operation(
                    "Prime Factors",
                    f"n={n}, result={result}"
                )
            else:
                print("Please enter an integer greater than 1.")

        elif choice == "6":
            start = validation.get_integer("Enter starting value: ")
            end = validation.get_integer("Enter ending value: ")

            if start > end:
                print("Starting value must not be greater than ending value.")
            else:
                result = factoring.pseudo_random_number(start, end)
                print("Pseudo-random number:", result)

                save_operation(
                    "Pseudo-Random Number",
                    f"range={start} to {end}, result={result}"
                )

        elif choice == "7":
            base = validation.get_integer("Enter base: ")
            exponent = validation.get_non_negative_integer(
                "Enter exponent: "
            )

            result = factoring.large_power(base, exponent)
            print("Result:", result)

            save_operation(
                "Large Power",
                f"base={base}, exponent={exponent}, result={result}"
            )

        elif choice == "8":
            n = validation.get_non_negative_integer("Enter n: ")

            result = factoring.nth_fibonacci(n)

            if result is None:
                print("Please enter a non-negative number.")
            else:
                print(f"The {n}th Fibonacci number is:", result)

                save_operation(
                    "Nth Fibonacci",
                    f"n={n}, result={result}"
                )

        elif choice == "9":
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 9.")


def arrays_menu():
    while True:
        print("\n========================================")
        print("             ARRAY ALGORITHMS")
        print("========================================")
        print("1. Reverse an Array")
        print("2. Count an Element")
        print("3. Find Maximum")
        print("4. Remove Duplicates")
        print("5. Partition an Array")
        print("6. Find Kth Smallest Element")
        print("7. Back to Algorithm Solver")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            numbers = validation.get_integer_list(
                "Enter numbers separated by spaces: "
            )

            result = arrays.reverse_array(numbers)
            print("Reversed array:", result)

            save_operation(
                "Reverse Array",
                f"array={numbers}, result={result}"
            )

        elif choice == "2":
            numbers = validation.get_integer_list(
                "Enter numbers separated by spaces: "
            )

            target = validation.get_integer(
                "Enter element to count: "
            )

            result = arrays.count_element(numbers, target)
            print("Count:", result)

            save_operation(
                "Count Element",
                f"array={numbers}, target={target}, result={result}"
            )

        elif choice == "3":
            numbers = validation.get_integer_list(
                "Enter numbers separated by spaces: "
            )

            result = arrays.find_maximum(numbers)

            if result is None:
                print("Array cannot be empty.")
            else:
                print("Maximum:", result)

                save_operation(
                    "Find Maximum",
                    f"array={numbers}, result={result}"
                )

        elif choice == "4":
            numbers = validation.get_integer_list(
                "Enter numbers separated by spaces: "
            )

            result = arrays.remove_duplicates(numbers)

            print("Array without duplicates:", result)

            save_operation(
                "Remove Duplicates",
                f"array={numbers}, result={result}"
            )

        elif choice == "5":
            numbers = validation.get_integer_list(
                "Enter numbers separated by spaces: "
            )

            pivot = validation.get_integer("Enter pivot value: ")

            result = arrays.partition_array(numbers, pivot)

            print("Partitioned array:", result)

            save_operation(
                "Partition Array",
                f"array={numbers}, pivot={pivot}, result={result}"
            )

        elif choice == "6":
            numbers = validation.get_integer_list(
                "Enter numbers separated by spaces: "
            )

            k = validation.get_positive_integer("Enter k: ")

            result = arrays.kth_smallest(numbers, k)

            if result is None:
                print("Invalid value of k.")
            else:
                print(f"{k}th smallest element:", result)

                save_operation(
                    "Kth Smallest",
                    f"array={numbers}, k={k}, result={result}"
                )

        elif choice == "7":
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


def collections_menu():
    while True:
        print("\n========================================")
        print("           PYTHON COLLECTIONS")
        print("========================================")
        print("1. List Operations")
        print("2. Tuple Operations")
        print("3. Set Operations")
        print("4. Dictionary Operations")
        print("5. Back to Algorithm Solver")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            numbers = validation.get_integer_list(
                "Enter numbers separated by spaces: "
            )

            result = collections.list_operations(numbers)
            print("List information:", result)

            save_operation(
                "List Operations",
                f"input={numbers}, result={result}"
            )

        elif choice == "2":
            numbers = validation.get_integer_list(
                "Enter numbers separated by spaces: "
            )

            result = collections.tuple_operations(numbers)
            print("Tuple information:", result)

            save_operation(
                "Tuple Operations",
                f"input={numbers}, result={result}"
            )

        elif choice == "3":
            numbers = validation.get_integer_list(
                "Enter numbers separated by spaces: "
            )

            result = collections.set_operations(numbers)
            print("Set information:", result)

            save_operation(
                "Set Operations",
                f"input={numbers}, result={result}"
            )

        elif choice == "4":
            numbers = validation.get_integer_list(
                "Enter numbers separated by spaces: "
            )

            result = collections.dictionary_operations(numbers)
            print("Dictionary frequency:", result)

            save_operation(
                "Dictionary Operations",
                f"input={numbers}, result={result}"
            )

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


def conversions_menu():
    while True:
        print("\n========================================")
        print("             BASE CONVERSION")
        print("========================================")
        print("1. Decimal to Binary")
        print("2. Decimal to Octal")
        print("3. Decimal to Hexadecimal")
        print("4. Binary to Decimal")
        print("5. Octal to Decimal")
        print("6. Hexadecimal to Decimal")
        print("7. Back to Algorithm Solver")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            number = validation.get_non_negative_integer(
                "Enter decimal number: "
            )

            result = conversions.decimal_to_base(number, 2)
            print("Binary:", result)

            save_operation(
                "Decimal to Binary",
                f"number={number}, result={result}"
            )

        elif choice == "2":
            number = validation.get_non_negative_integer(
                "Enter decimal number: "
            )

            result = conversions.decimal_to_base(number, 8)
            print("Octal:", result)

            save_operation(
                "Decimal to Octal",
                f"number={number}, result={result}"
            )

        elif choice == "3":
            number = validation.get_non_negative_integer(
                "Enter decimal number: "
            )

            result = conversions.decimal_to_base(number, 16)
            print("Hexadecimal:", result)

            save_operation(
                "Decimal to Hexadecimal",
                f"number={number}, result={result}"
            )

        elif choice == "4":
            number = input("Enter binary number: ")

            try:
                result = conversions.base_to_decimal(number, 2)
                print("Decimal:", result)

                save_operation(
                    "Binary to Decimal",
                    f"number={number}, result={result}"
                )

            except ValueError:
                print("Invalid binary number.")

        elif choice == "5":
            number = input("Enter octal number: ")

            try:
                result = conversions.base_to_decimal(number, 8)
                print("Decimal:", result)

                save_operation(
                    "Octal to Decimal",
                    f"number={number}, result={result}"
                )

            except ValueError:
                print("Invalid octal number.")

        elif choice == "6":
            number = input("Enter hexadecimal number: ")

            try:
                result = conversions.base_to_decimal(number, 16)
                print("Decimal:", result)

                save_operation(
                    "Hexadecimal to Decimal",
                    f"number={number}, result={result}"
                )

            except ValueError:
                print("Invalid hexadecimal number.")

        elif choice == "7":
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


def algorithm_solver_menu():
    while True:
        print("\n========================================")
        print("             ALGORITHM SOLVER")
        print("========================================")
        print("1. Fundamental Algorithms")
        print("2. Factoring Algorithms")
        print("3. Array Algorithms")
        print("4. Python Collections")
        print("5. Base Conversions")
        print("6. Back to Main Menu")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            fundamental_menu()

        elif choice == "2":
            factoring_menu()

        elif choice == "3":
            arrays_menu()

        elif choice == "4":
            collections_menu()

        elif choice == "5":
            conversions_menu()

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


def learning_menu():
    while True:
        print("\n========================================")
        print("             LEARNING MODULE")
        print("========================================")
        print("1. Learn Factorial")
        print("2. Learn Fibonacci")
        print("3. Learn GCD")
        print("4. Back to Main Menu")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            explanations.show_factorial()

        elif choice == "2":
            explanations.show_fibonacci()

        elif choice == "3":
            explanations.show_gcd()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


def practice_menu():
    score = 0
    total_questions = 0

    while True:
        print("\n========================================")
        print("             PRACTICE MODE")
        print("========================================")
        print("1. Start Practice")
        print("2. View Score")
        print("3. Back to Main Menu")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            question, answer = questions.generate_question()

            print("\nQuestion:")
            print(question)

            user_answer = validation.get_integer("Your answer: ")

            total_questions += 1

            if user_answer == answer:
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
                print("Correct answer:", answer)

        elif choice == "2":
            print("\nScore:", score, "/", total_questions)

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 3.")


def performance_menu():
    while True:
        print("\n========================================")
        print("          PERFORMANCE ANALYSIS")
        print("========================================")
        print("1. Measure Factorial")
        print("2. Measure Fibonacci")
        print("3. Measure Prime Generation")
        print("4. Measure Array Maximum")
        print("5. Back to Main Menu")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            n = validation.get_non_negative_integer(
                "Enter a number: "
            )

            result, execution_time = performance.measure_execution_time(
                fundamental.factorial,
                n
            )

            print("Result:", result)
            print("Execution time:", execution_time, "seconds")

        elif choice == "2":
            n = validation.get_non_negative_integer(
                "Enter number of Fibonacci terms: "
            )

            result, execution_time = performance.measure_execution_time(
                fundamental.fibonacci_sequence,
                n
            )

            print("Result:", result)
            print("Execution time:", execution_time, "seconds")

        elif choice == "3":
            n = validation.get_non_negative_integer(
                "Generate primes up to: "
            )

            result, execution_time = performance.measure_execution_time(
                factoring.generate_primes,
                n
            )

            print("Prime numbers:", result)
            print("Execution time:", execution_time, "seconds")

        elif choice == "4":
            numbers = validation.get_integer_list(
                "Enter numbers separated by spaces: "
            )

            result, execution_time = performance.measure_execution_time(
                arrays.find_maximum,
                numbers
            )

            print("Maximum:", result)
            print("Execution time:", execution_time, "seconds")

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


def history_menu():
    while True:
        print("\n========================================")
        print("                HISTORY")
        print("========================================")
        print("1. View History")
        print("2. Save History")
        print("3. Load History")
        print("4. Clear History")
        print("5. Back to Main Menu")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            records = history.get_history()

            if records:
                print("\n--- History ---")

                for record in records:
                    print(record)
            else:
                print("\nNo history available.")

        elif choice == "2":
            records = history.get_history()

            file_manager.save_history(records)

            print("History saved successfully.")

        elif choice == "3":
            records = file_manager.load_history()

            history.set_history()

            print("History loaded successfully.")

            

        elif choice == "4":
            history.clear_history()
            print("History cleared.")

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


def main():
    while True:
        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            algorithm_solver_menu()

        elif choice == "2":
            learning_menu()

        elif choice == "3":
            practice_menu()

        elif choice == "4":
            performance_menu()

        elif choice == "5":
            history_menu()

        elif choice == "6":
            print("\n========================================")
            print("                    HELP")
            print("========================================")
            print("ALGO-X is an interactive algorithm")
            print("learning and problem-solving toolkit.")
            print()
            print("Use Algorithm Solver to execute algorithms.")
            print("Use Learning Module to study algorithms.")
            print("Use Practice Mode to test your knowledge.")
            print("Use Performance Analysis to measure execution time.")
            print("Use History to view and save previous operations.")
            print("========================================")

        elif choice == "7":
            print("\nThank you for using ALGO-X!")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()