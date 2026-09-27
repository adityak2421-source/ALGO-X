import unittest
from Algorithms import collections


class TestCollections(unittest.TestCase):

    def test_list_operations(self):
        result = collections.list_operations([1, 2, 3])

        self.assertEqual(result["length"], 3)
        self.assertEqual(result["first_element"], 1)
        self.assertEqual(result["last_element"], 3)

    def test_tuple_operations(self):
        result = collections.tuple_operations([1, 2, 3])

        self.assertEqual(result["tuple"], (1, 2, 3))
        self.assertEqual(result["length"], 3)

    def test_set_operations(self):
        result = collections.set_operations([1, 2, 2, 3])

        self.assertEqual(result["unique_count"], 3)

    def test_dictionary_operations(self):
        result = collections.dictionary_operations([1, 2, 2, 3, 3, 3])

        self.assertEqual(
            result,
            {1: 1, 2: 2, 3: 3}
        )


if __name__ == "__main__":
    unittest.main()