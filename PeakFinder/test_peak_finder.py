import unittest
from peak_finder import find_peak

class TestPeakFinder(unittest.TestCase):

    def test_peak_finder(self):
        arrays = {
            5: [1,2,3,4,5],
            6: [6,5,4,3,2,1],
            4: [1,2,3,4,3,2,1],
            3: [1,3,2,2,3,1],
            3: [2,2,3,3,3,5,3],
            100000: range(100001)
            }
        for value, array in arrays.items():
            self.assertEqual(value, find_peak(array))

    def test_peak_finder_empty_array(self):
        array = []
        self.assertEqual(False, find_peak(array))

    def test_peak_finder_single_element(self):
        array = [1]
        self.assertEqual(1, find_peak(array))

if __name__ == "__main__":
    unittest.main()
