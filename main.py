from Algorithms import fundamental 
from Algorithms import factoring


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
            a = int(input("Enter first value: "))
            b = int(input("Enter second value: "))

            result = fundamental.exchange_values(a, b)
            print("After exchange:", result)

        elif choice == "2":
            n = int(input("Enter a number: "))

            result = fundamental.count_numbers(n)
            print("Count:", result)

        elif choice == "3":
            n = int(input("Enter a number: "))

            result = fundamental.summation(n)
            print("Sum:", result)

        elif choice == "4":
            n = int(input("Enter a number: "))

            result = fundamental.factorial(n)
            print("Factorial:", result)

        elif choice == "5":
            n = int(input("How many Fibonacci numbers? "))

            result = fundamental.fibonacci_sequence(n)
            print("Fibonacci sequence:", result)

        elif choice == "6":
            n = int(input("Enter a number: "))

            result = fundamental.reverse_number(n)
            print("Reversed number:", result)

        elif choice == "7":
            character = input("Enter a digit character: ")

            result = fundamental.character_to_number(character)
            print("Number:", result)

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
            n = float(input("Enter a number: "))

            result = factoring.square_root(n)

            if result is None:
                print("Square root is not available for negative numbers.")
            else:
                print("Square root:", result)

        elif choice == "2":
            n = int(input("Enter an integer: "))

            result = factoring.smallest_divisor(n)

            if result is None:
                print("Please enter a number greater than 1.")
            else:
                print("Smallest divisor:", result)

        elif choice == "3":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))

            result = factoring.gcd(a, b)
            print("GCD:", result)

        elif choice == "4":
            n = int(input("Generate primes up to: "))

            result = factoring.generate_primes(n)
            print("Prime numbers:", result)

        elif choice == "5":
            n = int(input("Enter a number: "))

            result = factoring.prime_factors(n)

            if result:
                print("Prime factors:", result)
            else:
                print("Please enter an integer greater than 1.")

        elif choice == "6":
            start = int(input("Enter starting value: "))
            end = int(input("Enter ending value: "))

            if start > end:
                print("Starting value must not be greater than ending value.")
            else:
                result = factoring.pseudo_random_number(start, end)
                print("Pseudo-random number:", result)

        elif choice == "7":
            base = int(input("Enter base: "))
            exponent = int(input("Enter exponent: "))

            if exponent < 0:
                print("Please enter a non-negative exponent.")
            else:
                result = factoring.large_power(base, exponent)
                print("Result:", result)

        elif choice == "8":
            n = int(input("Enter n: "))

            result = factoring.nth_fibonacci(n)

            if result is None:
                print("Please enter a non-negative number.")
            else:
                print(f"The {n}th Fibonacci number is:", result)

        elif choice == "9":
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 9.")


def algorithm_solver_menu():
    while True:
        print("\n========================================")
        print("             ALGORITHM SOLVER")
        print("========================================")
        print("1. Fundamental Algorithms")
        print("2. Factoring Algorithms")
        print("3. Back to Main Menu")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            fundamental_menu()

        elif choice == "2":
            factoring_menu()

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 3.")
            

def main():
    while True:
        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            algorithm_solver_menu()
            
        elif choice == "2":
            print("\n[Learning Module]")
            print("This module will be added soon.")

        elif choice == "3":
            print("\n[Practice Mode]")
            print("This module will be added soon.")

        elif choice == "4":
            print("\n[Performance Analysis]")
            print("This module will be added soon.")

        elif choice == "5":
            print("\n[History]")
            print("This module will be added soon.")

        elif choice == "6":
            print("\n[Help]")
            print("ALGO-X is an interactive algorithm learning toolkit.")

        elif choice == "7":
            print("\nThank you for using ALGO-X!")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()