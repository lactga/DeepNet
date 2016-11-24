from unittest import TestCase
from src.activation_function.linear_logistic_function import linear_logistic_function


class TestLinear_logistic_function(TestCase):

    def test_0(self):
        self.assertEqual(linear_logistic_function(-5), -1)

    def test_1(self):
        self.assertEqual(linear_logistic_function(5), 1)

    def test_0(self):
        self.assertEqual(linear_logistic_function(0), 0)

    def test_05(self):
        self.assertEqual(linear_logistic_function(1/2), 1/2)

    def test_minus05(self):
        self.assertEqual(linear_logistic_function(-1/2), -1/2)
