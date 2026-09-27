def show_factorial():
    print("\n========================================")
    print("              FACTORIAL")
    print("========================================")

    print("Description:")
    print("Factorial of n is the product of all positive")
    print("integers from 1 to n.")

    print("\nExample:")
    print("5! = 1 × 2 × 3 × 4 × 5 = 120")

    print("\nPseudocode:")
    print("START")
    print("Input n")
    print("Set result = 1")
    print("For i from 1 to n")
    print("    result = result × i")
    print("Display result")
    print("END")

    print("\nTime Complexity: O(n)")
    print("Space Complexity: O(1)")


def show_fibonacci():
    print("\n========================================")
    print("              FIBONACCI")
    print("========================================")

    print("Description:")
    print("Each Fibonacci number is obtained by adding")
    print("the previous two numbers.")

    print("\nExample:")
    print("0, 1, 1, 2, 3, 5, 8, 13...")

    print("\nPseudocode:")
    print("START")
    print("Input n")
    print("Set a = 0 and b = 1")
    print("Repeat n times")
    print("    Display a")
    print("    Set a, b = b, a + b")
    print("END")

    print("\nTime Complexity: O(n)")
    print("Space Complexity: O(n)")


def show_gcd():
    print("\n========================================")
    print("                GCD")
    print("========================================")

    print("Description:")
    print("GCD finds the greatest number that divides")
    print("two given numbers exactly.")

    print("\nExample:")
    print("GCD(12, 18) = 6")

    print("\nPseudocode:")
    print("START")
    print("Input a and b")
    print("While b is not 0")
    print("    Set a, b = b, a mod b")
    print("Display a")
    print("END")

    print("\nTime Complexity: O(log n)")
    print("Space Complexity: O(1)")