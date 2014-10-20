import unittest


from solution import simplify_fraction


class TestSimplifyFraction(unittest.TestCase):

    def test_simplify_fraction(self):
        self.assertEqual(simplify_fraction((3, 9)), (1, 3))
        self.assertEqual(simplify_fraction((1, 7)), (1, 7))
        self.assertEqual(simplify_fraction((63, 462)), (3, 22))
        self.assertEqual(simplify_fraction((4, 10)), (2, 5))


if __name__ == "__main__":
    unittest.main()

