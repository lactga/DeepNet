import numpy as np
from unittest import TestCase
from src.error_function.binary_classification_log_likelihood import binary_classification_log_likelihood


class TestLogistic_function(TestCase):

    def test_same(self):
        x = np.array([0, 0, 0])
        y = np.array([0, 0, 0])
        self.assertEqual(binary_classification_log_likelihood(x, y), 0)

    def test_case1(self):
        x = np.array([0, 0, 1])
        y = np.array([0, 0, 0])
        self.assertEqual(binary_classification_log_likelihood(x, y), float('Inf'))

    def test_case2(self):
        x = np.array([0.5, 0.5, 0.5])
        y = np.array([1, 0, 0])
        self.assertEqual(binary_classification_log_likelihood(x, y), -3 * np.log(0.5))

    def test_error1(self):
        x = np.array([1, 0, 0])
        y = np.array([1, 0])
        with self.assertRaises(ValueError):
            binary_classification_log_likelihood(x, y)

    def test_error2(self):
        x = [1, 0, 0]
        y = [1, 0, 0]
        with self.assertRaises(AttributeError):
            binary_classification_log_likelihood(x, y)

    def test_error3(self):
        x = None
        y = np.array([1, 0, 0])
        with self.assertRaises(TypeError):
            binary_classification_log_likelihood(x, y)

    def test_error4(self):
        x = np.array([])
        y = np.array([])
        with self.assertRaises(ValueError):
            binary_classification_log_likelihood(x, y)

    def test_error5(self):
        """
        0, 1の2値でないケース
        """
        x = np.array([1, 0, 0])
        y = np.array([1, -1, -1])
        with self.assertRaises(ValueError):
            binary_classification_log_likelihood(x, y)

