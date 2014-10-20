import unittest


from solution import nth_fib_lists


class TestNthFibList(unittest.TestCase):

    def test_correctness(self):
        self.assertEqual(nth_fib_lists([1], [2], 1), [1])
        self.assertEqual(nth_fib_lists([1], [2], 2), [2])
        self.assertEqual(nth_fib_lists([], [1, 2, 3], 4), [1, 2, 3, 1, 2, 3])
        self.assertEqual(nth_fib_lists([1, 2], [1, 3], 3), [1, 2, 1, 3])


if __name__ == '__main__':
    unittest.main()

