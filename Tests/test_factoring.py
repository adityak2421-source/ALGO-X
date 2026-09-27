import unittest
from Algorithms import factoring


class TestFactoring(unittest.TestCase):

    def test_smallest_divisor(self):
        self.assertEqual(
            factoring.smallest_divisor(15),
            3
        )

    def test_gcd(self):
        self.assertEqual(
            factoring.gcd(12, 18),
            6
        )

    def test_generate_primes(self):
        self.assertEqual(
            factoring.generate_primes(10),
            [2, 3, 5, 7]
        )

    def test_prime_factors(self):
        self.assertEqual(
            factoring.prime_factors(12),
            [2, 2, 3]
        )

    def test_large_power(self):
        self.assertEqual(
            factoring.large_power(2, 10),
            1024
        )

    def test_nth_fibonacci(self):
        self.assertEqual(
            factoring.nth_fibonacci(7),
            13
        )


if __name__ == "__main__":
    unittest.main()