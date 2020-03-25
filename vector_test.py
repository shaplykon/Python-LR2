import unittest
from vector import Vector


class vector_test(unittest.TestCase):
    def setUp(self):
        self.first_vector = Vector(2, [1, 1])
        self.second_vector = Vector(2, [2, 2])

    def test_add(self):
        self.assertEqual(self.first_vector.__add__(self.second_vector), Vector(2, [3, 3]),
                         "Add method does not work normally")

    def test_vector_mul(self):
        self.assertEqual(self.first_vector.__mul__(self.second_vector), 4,
                         "Vector multiplication does not work normally")

    def test_scalar_mul(self):
        self.assertEqual(self.first_vector.__mul__(2), self.second_vector,
                         "Vector multiplication does not work normally")

    def test_sub(self):
        self.assertEqual(self.second_vector.__sub__(self.first_vector), self.first_vector)


if __name__ == "__main__":
    unittest.main()
