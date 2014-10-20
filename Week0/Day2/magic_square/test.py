import unittest

from solution import magic_square


class TestMagicSquare(unittest.TestCase):

    def test_correctness(self):
        self.assertFalse(magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        self.assertTrue(magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))

        self.assertFalse(magic_square([[23, 28, 22], [22, 24, 27], [27, 21, 25]]))

        self.assertFalse(magic_square([[1, 2, 3], [4, 1, 1], [1, 3, 1]]))


if __name__ == "__main__":
    unittest.main()

