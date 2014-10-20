import unittest


from solution import sort_fractions


class TestCompareFractions(unittest.TestCase):

    def test_sort_fractions(self):
        self.assertEqual(sort_fractions([(2, 3), (1, 2), (1, 5), (1, 2)]),
                         [(1, 5), (1, 2), (1, 2), (2, 3)])


if __name__ == '__main__':
    unittest.main()

