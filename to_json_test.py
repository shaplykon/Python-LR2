import unittest
import to_json


class to_json_test(unittest.TestCase):
    def test_get_values(self):
        self.assertEqual(to_json.get_values([1, 2]), "1, 2", "get_values method does not work correctly")

    def test_get_object_by_id(self):
        obj = [1, 2]
        self.assertEqual(to_json.objects_by_id(id(obj)), obj)

    def test_to_json(self):
        test_object = []
        obj = to_json.to_json(test_object)
        self.assertIsInstance(obj, str)


if __name__ == "__main__":
    unittest.main()
