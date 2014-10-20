import unittest


from solution import groupby


class TestGroupby(unittest.TestCase):

    def test_groupby(self):
        odd_even = groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(odd_even, {0: [0, 2, 4, 6], 1: [1, 3, 5, 7]})


if __name__ == '__main__':
    unittest.main()

