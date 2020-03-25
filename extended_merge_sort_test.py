import unittest
import extended_merge_sort


class extended_merge_sort_test(unittest.TestCase):
    def test_change_output(self):
        self.assertIsInstance(extended_merge_sort.change_input("1.txt"), str)

    def test_change_input(self):
        self.assertIsInstance(extended_merge_sort.change_output("1.txt"), str)

    def test_merge_sort(self):
        arr = [2, 3, 1]
        extended_merge_sort.merge_sort(arr)
        self.assertEqual(arr, [1, 2, 3])



if __name__ == "__main__":
    unittest.main()
