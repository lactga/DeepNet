from unittest import TestCase
from src.activation_function.identity_function import identity_function


class TestIdentity_function(TestCase):

    def test_0(self):
        self.assertEqual(identity_function(0), 0)

    def test_plus(self):
        self.assertEqual(identity_function(5), 5)

    def test_minus(self):
        self.assertEqual(identity_function(-5), -5)
