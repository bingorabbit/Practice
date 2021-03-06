import unittest
from merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):
    def test_normal_behaviour(self):
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], merge_sort([9, 8, 5, 1, 2, 3, 0, 4, 7, 6]))

    def test_negative_list(self):
        self.assertEqual([-5, -4, -3, -2, -1, 0], merge_sort([-1, 0, -4, -3, -5, -2]))

    def test_single_element_list(self):
        self.assertEqual([1], merge_sort([1]))

    def test_empty_list(self):
        self.assertEqual([], merge_sort([]))


if __name__ == "__main__":
    unittest.main()
