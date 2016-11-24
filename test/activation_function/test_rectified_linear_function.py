from unittest import TestCase
from src.activation_function.rectified_linear_function import rectified_linear_function


class TestRectified_function(TestCase):

    def test_minus(self):
        self.assertEqual(rectified_linear_function(-5), 0)

    def test_plus(self):
        self.assertEqual(rectified_linear_function(5), 5)

    def test_0(self):
        self.assertEqual(rectified_linear_function(0), 0)
