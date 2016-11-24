import numpy as np
from unittest import TestCase
from src.error_function.mse import mse


class TestLogistic_function(TestCase):

    def test_same(self):
        x = np.array([1, 2, 3])
        y = np.array([1, 2, 3])
        self.assertEqual(mse(x, y), 0)

    def test_case1(self):
        x = np.array([1, 2, -1])
        y = np.array([0, 0, 0])
        self.assertEqual(mse(x, y), 2)

    def test_case2(self):
        x = np.array([1, 2, -1])
        y = np.array([-1, 0, 2])
        self.assertEqual(mse(x, y), 17/3)

    def test_error1(self):
        x = np.array([1, 2, 3])
        y = np.array([1, 2])
        with self.assertRaises(ValueError):
            mse(x, y)

    def test_error2(self):
        x = [1, 2, 3]
        y = [1, 2, 3]
        with self.assertRaises(TypeError):
            mse(x, y)

    def test_error3(self):
        x = None
        y = [1, 2, 3]
        with self.assertRaises(TypeError):
            mse(x, y)

    def test_error4(self):
        x = np.array([])
        y = np.array([])
        with self.assertRaises(ValueError):
            mse(x, y)

