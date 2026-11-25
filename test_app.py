import unittest
from app import calculate_total


class TestApplication(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate_total(10, 20), 30)

    def test_zero(self):
        self.assertEqual(calculate_total(0, 0), 0)

    def test_negative(self):
        self.assertEqual(calculate_total(-5, 5), 0)


if __name__ == "__main__":
    unittest.main()
