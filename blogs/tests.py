from django.test import TestCase


class RandomTest(TestCase):
    def test_basic(self):
        self.assertNotEqual(9,0)
