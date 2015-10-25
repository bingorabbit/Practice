import unittest
import array_inversions

class TestArrayInversions(unittest.TestCase):

    def test_array_inversions(self):
        arrays = [
            [0, []],
            [0, [1]],
            [1, [2,1]],
            [1, [1,3,2]],
            [3, [3,2,1]],
            [6, [3,2,1,6,5,4]],
            [15, [6,5,4,3,2,1]],
            [0, [1,2,3,4,5,6]],
            [5, [3,2,4,1,6,5]],
            [1, [1,2,3,4,6,5]]
        ]
        for a in arrays:
            self.assertEqual(a[0], array_inversions.count_inversions(a[1])[1])


if __name__ == "__main__":
    unittest.main()