import unittest
from Algorithms import arrays


class TestArrays(unittest.TestCase):

    def test_reverse_array(self):
        self.assertEqual(
            arrays.reverse_array([1, 2, 3]),
            [3, 2, 1]
        )

    def test_count_element(self):
        self.assertEqual(
            arrays.count_element([1, 2, 2, 3], 2),
            2
        )

    def test_find_maximum(self):
        self.assertEqual(
            arrays.find_maximum([4, 8, 2, 6]),
            8
        )

    def test_remove_duplicates(self):
        self.assertEqual(
            arrays.remove_duplicates([1, 2, 2, 3, 3]),
            [1, 2, 3]
        )

    def test_partition(self):
        self.assertEqual(
            arrays.partition_array([5, 2, 8, 1], 5),
            [2, 1, 5, 8]
        )

    def test_kth_smallest(self):
        self.assertEqual(
            arrays.kth_smallest([5, 2, 8, 1], 2),
            2
        )


if __name__ == "__main__":
    unittest.main()