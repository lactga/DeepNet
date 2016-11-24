from unittest import TestCase
from src.activation_function.logistic_function import logistic_function


class TestLogistic_function(TestCase):

    def test_0(self):
        self.assertEqual(logistic_function(-float('Inf')), 0)

    def test_1(self):
        self.assertEqual(logistic_function(float('Inf')), 1)

    def test_05(self):
        self.assertEqual(logistic_function(0), 1/2)
