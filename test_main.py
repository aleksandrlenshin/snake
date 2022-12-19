from unittest import TestCase
from main import func1, func2

class Test(TestCase):
    def test_func1(self):
        self.a ssertEqual(
            func1(), None
        )

    def test_func2(self):
        self.assertEqual(
            func2(), None
        )
