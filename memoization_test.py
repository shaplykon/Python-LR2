import unittest
import memoization
import inspect


class vector_test(unittest.TestCase):
    def test_squaring(self):
        self.assertEqual(memoization.squaring(2), 4)

    def test_memoization(self):
        self.assertEqual(inspect.isfunction(memoization.memoization(memoization.squaring)), True)


if __name__ == "__main__":
    unittest.main()
