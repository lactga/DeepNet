from unittest import TestCase
from src.activation_function.hyperbolic_tangent import hyperbolic_tangent


class TestHyperbolic_tangent(TestCase):

    def test_minus1(self):
        self.assertEqual(hyperbolic_tangent(-float('Inf')), -1)

    def test_1(self):
        self.assertEqual(hyperbolic_tangent(float('Inf')), 1)

    def test_0(self):
        self.assertEqual(hyperbolic_tangent(0), 0)
