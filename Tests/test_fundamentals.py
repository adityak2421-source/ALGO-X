import unittest
from Algorithms import fundamental


class TestFundamental(unittest.TestCase):

    def test_exchange_values(self):
        self.assertEqual(
            fundamental.exchange_values(10, 20),
            (20, 10)
        )

    def test_count_numbers(self):
        self.assertEqual(
            fundamental.count_numbers(5),
            5
        )

    def test_summation(self):
        self.assertEqual(
            fundamental.summation(5),
            15
        )

    def test_factorial(self):
        self.assertEqual(
            fundamental.factorial(5),
            120
        )

    def test_fibonacci(self):
        self.assertEqual(
            fundamental.fibonacci_sequence(6),
            [0, 1, 1, 2, 3, 5]
        )

    def test_reverse_number(self):
        self.assertEqual(
            fundamental.reverse_number(1234),
            4321
        )

    def test_character_to_number(self):
        self.assertEqual(
            fundamental.character_to_number("7"),
            7
        )


if __name__ == "__main__":
    unittest.main()